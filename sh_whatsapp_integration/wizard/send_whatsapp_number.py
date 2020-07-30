# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class sh_send_whatsapp_number(models.TransientModel):
    _name = "sh.send.whatsapp.number.wizard"
    _description = "Send whatsapp message wizard"
    
    partner_ids = fields.Many2one("res.partner", string = "Recipients")
    whatsapp_mobile = fields.Char(string = "Whatsapp Number", required=True)
    message = fields.Text("Message", required=True)
    crm_lead_id = fields.Many2one('crm.lead',string="Lead")
    ticket_id = fields.Many2one('helpdesk.ticket', string="Ticket")
    template_id = fields.Many2one('whatsapp.template',string="Template")
    
    @api.onchange('partner_ids')
    def onchange_partner(self):
        if self.partner_ids:
            self.whatsapp_mobile = self.partner_ids.mobile
   
    @api.onchange('template_id')
    def onchange_template_id(self):
        if self.template_id:
            self.message = self.template_id.body
    
    @api.multi
    def action_send_whatsapp_number(self):
        for rec in self:
            if rec.partner_ids:
                sh_message=""
                if self.message:
                    sh_message =  str(self.message).replace('*','').replace('_','').replace('%0A','<br/>').replace('%20',' ')
                if self.crm_lead_id and self.crm_lead_id.company_id.crm_lead_display_in_message:
                    self.env['mail.message'].create({
                                                    'partner_ids':[(4, rec.partner_ids.id)] or False,
                                                    'model':'res.partner',
                                                    'res_id':rec.partner_ids.id,
                                                    'author_id':self.env.user.partner_id.id,
                                                    'body':sh_message,
                                                    'message_type':'notification'
                                                })
                if self.ticket_id:
                    self.env['mail.message'].create({
                                                    'partner_ids':[(4, rec.partner_ids.id)] or False,
                                                    'model':'helpdesk.ticket',
                                                    'res_id':self.ticket_id.id,
                                                    'author_id':self.env.user.partner_id.id,
                                                    'body':sh_message,
                                                    'message_type':'notification'
                                                })
                return {
                    'type': 'ir.actions.act_url',
                    'url': "https://web.whatsapp.com/send?l=&phone="+rec.whatsapp_mobile+"&text=" + self.message,
                    'target': 'new'
                }
                    
        