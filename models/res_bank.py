import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class ResBank(models.Model):
    _inherit = 'res.bank'

    branch_ids = fields.One2many('res.bank.branch', 'bank_id', string="Branch", readonly=True)

    branch_ids_count = fields.Integer(
        string='Branch Count',
        compute='_compute_branch_ids_count',
    )

    def _compute_branch_ids_count(self):
        for bank in self:
            bank.branch_ids_count = len(bank.branch_ids)

    def action_view_branches(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Branches',
            'res_model': 'res.bank.branch',
            'view_mode': 'list,form',
            'domain': [('bank_id', '=', self.id)],
            'context': {'default_bank_id': self.id},
        }