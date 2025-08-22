import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)

class Token(models.Model):
    _name = 'api.token'
    _description = 'API Token Management'

    name = fields.Char(string='Token Name', required=True)
    access_token = fields.Char(string='Token Value', required=True, unique=True)
    refresh_token = fields.Char(string='Refresh Token', required=True, unique=True)