import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)

class Player(models.Model):
    _name = 'player'
    _description = 'Player'

    name = fields.Char(string='Name')
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    age = fields.Integer(string="Age", default=1)

    def validate_name(self, vals):
        if vals['first_name'] is not None or vals['last_name'] is not None:
            name = f"{vals['first_name']} {vals['last_name']}"

            player = self.env['player'].search([('name', '=', name)], limit=1)
            if player:
                _logger.info(f"====== player =====>{player.read()[0]}")
                raise ValidationError(f"Player already exists: {player.name} ({player.age} years old)")
            
            vals['name'] = name
        
        return vals
        
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals = self.validate_name(vals)
        return super(Player, self).create(vals_list)
    
    def write(self, vals):
        _logger.info(f"====== self =====>{self.read()}")
        _logger.info(f"====== vals =====>{vals}")
        if 'first_name' not in vals:
            vals['first_name'] = self.first_name
        if 'last_name' not in vals:
            vals['last_name'] = self.last_name

        vals = self.validate_name(vals)
        return super(Player, self).write(vals)