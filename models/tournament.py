import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)

class Tournament(models.Model):
    _name = 'tournament'
    _description = 'Tournament'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    date_time = fields.Datetime(string='Date from', required=True)
    date_time_to = fields.Datetime(string='Date to', required=True)
    game = fields.Char(string='Game', required=True)
    players = fields.Many2many('player', string='Players')
    max_players = fields.Integer(string='Max Players', default=16)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')
    winner_id = fields.Many2one('player', string='Winner', readonly=True)
    description = fields.Text(string='Description')
    organizer_id = fields.Many2one('res.users', string='Organizer', default=lambda self: self.env.user, readonly=True)
    organizer_email = fields.Char(string='Organizer Email', related='organizer_id.email', readonly=True)

    calendar_event = fields.Many2one('calendar.event', string="Event", required=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'max_players' in vals and vals['max_players'] <= 0:
                raise ValidationError(_("Max players must be greater than zero."))
        return super(Tournament, self).create(vals_list)
    
    def push_tournament_to_calendar(self):
        for tourn in self:
            calendar_event = {
                "name": tourn.name,
                "start": tourn.date_time,
                "stop": tourn.date_time_to,
                "location": tourn.location,
                "description": tourn.description
            }

            alarm = self.env['calendar.alarm'].search([('name', 'ilike', '1 Day')], limit=1)
            print(f"==>> alarm: {alarm}")
            if alarm:
                calendar_event['alarm_ids'] = [(6, 0, [alarm.id])] # Use this to add records or objects to a many2many or many2one field when creating or updating a record using a json dictionary.

            calendar_event = self.env['calendar.event'].create(calendar_event)
            print(f"==>> calendar_event: {calendar_event}")
            self.write({ "calendar_event": calendar_event.id })

            # this is how you create an alert in Odoo
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Calendar',
                    'message': "Event Created!",
                    'type': 'success',
                    'sticky': False,
                }
            }
        
    