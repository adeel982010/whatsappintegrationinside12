# -*- coding: utf-8 -*-
import requests
import xmltodict
from datetime import datetime
from odoo import models, fields, api, _


class ProjectContract(models.Model):
    _name = 'project.contract'
    _description = 'Project Contract'

    name = fields.Char('Name')


class Properties(models.Model):
    _name = 'properties'
    _description = 'Properties'

    name = fields.Char('Name')


class eWallet(models.Model):    
    _name = 'e.wallet'
    _description = 'eWallet'

    name = fields.Char('Name')
    payment_reference = fields.Char('Payment Reference')
    action = fields.Char('Action')
    eid = fields.Char('EID')
    opening_date = fields.Date('Opening Date')
    opening_balance = fields.Float('Opening Balance')
    has_prepaid = fields.Boolean('Has Prepaid')
    meter_account_ids = fields.One2many('meter.account', 'ewallet_id', string="Meter Accounts")
    mdms_server_id = fields.Many2one('mdms.server', string="MDMS Server")

    @api.multi
    def current_balance(self):
        if self.eid and self.opening_date and self.mdms_server_id:
            res = {
                'type': 'ir.actions.client',
                'name':'Balance History',
                'tag':'open_balance_history',
            }
            return res

    @api.multi
    def get_balance_history(self, start_date, end_date):
        if self and start_date and end_date:
            start_date += ' 00:00:00'
            end_date += ' 23:59:59'
            url = self.mdms_server_id.url + '/getLedger.jsp'
            params = {
                'eid': self.eid,
                'startdate': start_date,
                'enddate': end_date,
                'LOGIN': self.mdms_server_id.login,
                'PWD': self.mdms_server_id.password
            }
            try:
                res = requests.get(url=url, params=params)
                if res.text:
                    result = xmltodict.parse(res.text, dict_constructor=dict)
                    if result and result.get('xml') and result.get('xml').get('result'):
                        if result.get('xml').get('result') != 'SUCCESS':
                            return {'error': _(result.get('xml').get('result'))}
                        else:
                            return {'success': result.get('xml').get('transactions')}
            except:
                return {'error': _("Request Failed !!")}


class MeterAccount(models.Model):
    _name = 'meter.account'
    _inherit = ['mail.thread']
    _description = 'Meter Account'

    name = fields.Char('Name')
    partner_id = fields.Many2one('res.partner', string="Customer")
    meter_acc_no = fields.Char('Meter Account No.')
    region = fields.Char('Region')
    activation_date = fields.Date('Activation Date')
    eid = fields.Char('EID')
    financial_year_start = fields.Char('Financial Year Start')
    billing_period = fields.Char('Billing Period')
    lot_number = fields.Char('Lot Number')
    stand_number = fields.Char('Stand Number')
    utility_type = fields.Selection([('Electricity', 'Electricity'), ('Gas', 'Gas'), ('Water', 'Water'), ('Services', 'Services')], string="Utility Type")
    business_partner_id = fields.Many2one('project.contract', string="Business Partner")
    site_id = fields.Many2one('properties', string="Site")
    mdms_server = fields.Char('MDMS Server')
    ewallet_id = fields.Many2one('e.wallet', string="eWallet")
    meter_account_status = fields.Selection([
        ('Active', 'Active'),
        ('MOMI', 'MOMI'),
        ('Blocking', 'Blocking'),
        ('Adjustment', 'Adjustment'),
        ('Estimation', 'Estimation'),
        ('Do Not Disconnect', 'Do Not Disconnect')
    ], string="Meter Account Status", default="Active")
    meters_ids = fields.Many2many('meters', string="Meters")
    tarrifs_ids = fields.Many2many('tarrifs', string="Tarrifs")
