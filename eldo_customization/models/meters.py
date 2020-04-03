# -*- coding: utf-8 -*-
from odoo import models, fields


class Meters(models.Model):
	_name = 'meters'
	_inherit = ['mail.thread']
	_description = 'Meters'

	name = fields.Char('Meter Serial No.')
	meter_image = fields.Binary('Meter Image')
	name1 = fields.Char('Name')
	meter_status = fields.Selection([
		('Active', 'Active'),
		('Inactive','Inactive')
	], string="Meter Status")
	utility_type = fields.Selection([
		('Electricity', 'Electricity'),
		('Gas','Gas'),
		('Service', 'Service'),
		('Water','Water')
	], string="Utility Type")
	voltage_level = fields.Selection([
		('11 kV', '11 kV'),
		('6.6 kV','6.6 kV'),
		('0.4 kV', '0.4 kV')
	], string="Voltage Level")
	meter_type = fields.Char('Meter Type')
	longitude = fields.Char('Longitude')
	connection_type = fields.Selection([
		('CT/VT', 'CT/VT'),
		('CT Only','CT Only'),
		('DC', 'DC'),
		('VM','VM')
	], string="Connection Type")
	latitude = fields.Char('Latitude')
	last_communication_date = fields.Datetime('Last Communication Date')
	installation_date = fields.Date('Installation Date')
	site_id = fields.Many2one('properties', string="Site")
	activation_date = fields.Date('Activation Date')
	business_partner_id = fields.Many2one('project.contract', string="Business Partner")
	mdms_server = fields.Char('MDMS Server')
	common_area = fields.Boolean('Common Area')
	meter_account_number_ids = fields.Many2many('meter.account', string="Meter Account Numbers")
	multidropid = fields.Char('Multidrop ID')
	vt_ratio = fields.Char('VT Ratio')
	primary_meeting = fields.Selection([
		('Yes', 'Yes'),
		('No','No')
	], string="Primary Meeting")
	ct_ratio = fields.Char('CT Ratio')
	breaker_size = fields.Char('Breaker Size')
	number_of_phase = fields.Selection([
		('Single Phase', 'Single Phase'),
		('3 Phase','3 Phase')
	], string="Number Of Phases")
	network_access_media = fields.Selection([
		('PLC', 'PLC'),
		('RF','RF'),
		('RS 232', 'RS 232'),
		('RS 585','RS 585')
	], string="Network Access Media")
	sim_iccid = fields.Char('SIM ICCID')
	network_access_protocol = fields.Selection([
		('IEC62053', 'IEC62053'),
		('DLMS','DLMS'),
		('HDLC', 'HDLC'),
		('Modbus','Modbus'),
		('Mbus', 'Mbus'),
		('MPulse','MPulse'),
		('G3 Prime', 'G3 Prime'),
		('Sigfox','Sigfox')
	], string="Network Access Protocol")
	sim_phone_number = fields.Char('SIM Phone Number')
	ip_number = fields.Char('IP Number')
	sample_period = fields.Char('Sample Period')
	port_number = fields.Char('Port Number')
	sim_card_status = fields.Selection([
		('Active Line', 'Active Line'),
		('Active Test','Active Test'),
		('Inactive', 'Inactive')
	], string="SIM Card Status")
	modem_type = fields.Char('Modem Type')
	modem_brand = fields.Selection([
		('Recktron', 'Recktron'),
		('Billing Online','Billing Online'),
		('Kocos', 'Kocos')
	], string="Modem Brand")
	modem_number = fields.Char('Modem Number')
	meter_brand = fields.Selection([
		('ELSTER', 'ELSTER'),
		('EDMI','EDMI'),
		('ENERMAX', 'ENERMAX'),
		('BLUESTAR','BLUESTAR'),
		('LANDIS & GYR', 'LANDIS & GYR'),
		('SIEMENS','SIEMENS'),
		('PREMIER', 'PREMIER'),
		('SDG','SDG'),
		('ELSTER WATER', 'ELSTER WATER'),
		('Holley','Holley'),
		('Hexing', 'Hexing')
	], string="Meter Brand")
	vm_summation = fields.Char('VM Summation')
	model = fields.Char('Model')
	calibration_number = fields.Char('Calibration Number')
	maximum_demand = fields.Char('Maximum Demand')
	load_factor = fields.Char('Load Factor')
	place = fields.Char('Place')
	site = fields.Char('Site')
	zone = fields.Char('Zone')
	sub_status = fields.Selection([
		('operational','operational'),
		('network_failure', 'Network Failure'),
		('hardware_failure','Hardware Failure')
	], string="Sub Status", default="operational")
