import logging

from odoo import models, fields, api, _

class ResBankBranch(models.Model):
    _name = 'res.bank.branch'
    _description = 'Bank Branch Information'
    _order = 'branch_code'

    bank_id = fields.Many2one('res.bank', string="Bank")
    name = fields.Char(string='Branch Name', translate=False)
    branch_code = fields.Char(string='Branch Code', translate=False)
    website = fields.Char(string='Website', translate=False)
    address = fields.Text(string='Address', translate=False)
    phone = fields.Char(string='Phone', translate=False)
    swift_code = fields.Char(string='Swift Code', translate=False)
    country = fields.Many2one('res.country', string='Country')