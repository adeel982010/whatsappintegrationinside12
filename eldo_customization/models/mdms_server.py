# -*- coding: utf-8 -*-
from odoo import models, fields


class MDMSServer(models.Model):
    _name = 'mdms.server'
    _description = 'MDMS Server'

    name = fields.Char('Name')
    url = fields.Char('URL')
    login = fields.Char('Login')
    password = fields.Char('Password')
