# -*- coding: utf-8 -*-
from odoo import models, fields


class HelpdeskTicketType(models.Model):
    _inherit = 'helpdesk.ticket.type'

    helpdesk_team_ids = fields.Many2many('helpdesk.team', string="Helpdesk Teams")
