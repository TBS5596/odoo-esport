import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    is_preferred = fields.Boolean(string="Preferred Bank", default=False)

    branch_id = fields.Many2one('res.bank.branch', string="Branch")

    branch = fields.Char(string="Branch Name", copy=True, related="branch_id.name", store=True, readonly=True)
    branch_code = fields.Char(string="Branch Code", copy=True, related="branch_id.branch_code", store=True, readonly=True)
    swift_code = fields.Char(string="Swift Code", copy=True, related="branch_id.swift_code", store=True, readonly=True)

    # @api.onchange('branch_id')
    # def compute_branch_details(self):
    #     for record in self:
    #         if record.branch_id:
    #             record.branch = record.branch_id.name
    #             record.branch_code = record.branch_id.branch_code
    #             record.swift_code = record.branch_id.swift_code

    #         else:
    #             record.branch = record.branch_code = record.swift_code = ''