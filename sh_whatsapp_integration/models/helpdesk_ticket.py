# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
   
    mobile = fields.Char(string="Mobile", related="partner_id.mobile")

class HelpdeskWhatsappTemplate(models.Model):
    _name = 'whatsapp.template'
    _description = "WhatsApp Template"

    name = fields.Char(string="Name", required=True)
    body = fields.Text(string="Body", required=True)
    
