# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
   
    stage_name = fields.Char(string="Stage", related="stage_id.name")

    @api.model
    def message_new(self, msg, custom_values=None):
        values = dict(custom_values or {}, partner_email=msg.get('from'), partner_id=msg.get('author_id'))
        ticket = super(HelpdeskTicket, self).message_new(msg, custom_values=values)

        partner_ids = [x for x in ticket._find_partner_from_emails(self._ticket_email_split(msg)) if x]
        customer_ids = ticket._find_partner_from_emails(tools.email_split(values['partner_email']))
        partner_ids += customer_ids

        if customer_ids and not values.get('partner_id'):
            ticket.partner_id = customer_ids[0]
        if partner_ids:
            ticket.message_subscribe(partner_ids)
        ticket.update({'stage_id': self.env.ref('eldo_customization.stage_new_email').id})
        return ticket

    @api.multi
    def message_update(self, msg, update_vals):
        res = super(HelpdeskTicket, self).message_update(msg=msg, update_vals=update_vals)
        self.write({'stage_id': self.env.ref('eldo_customization.stage_new_email').id})
        return res
