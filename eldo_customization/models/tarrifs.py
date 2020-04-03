# -*- coding: utf-8 -*-
from odoo import models, fields


class Tarrifs(models.Model):
	_name = 'tarrifs'
	_description = 'Tarrifs'

	name = fields.Char('Tarrif')
	start_date = fields.Date('Start Date')
	default = fields.Boolean('Default')
	notified_demand = fields.Boolean('Notified Demand')
	meter_account_number_ids = fields.Many2many('meter.account', string="Meter Account Numbers")
	
