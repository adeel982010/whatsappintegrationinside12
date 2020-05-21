# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import UserError
import os

static_dict_theme = {
    '$o-enterprise-color': '#875A7B',
}


class ResCompany(models.Model):
    _inherit = "res.company"

    color = fields.Char(string="Color")

    def write(self, vals):
        res = super(ResCompany, self).write(vals)
        if vals.get('color'):
            company_id = self.env.user.company_id.id
            self.env['web.theme'].set_customize_theme(company_id)
        return res 


class WebTheme(models.Model):
    _name = "web.theme"
    _description = "Web Theme"

    def replace_file(self, file_path, static_dict):
        try:
            with open(file_path, 'w+') as new_file:
                for key, value in static_dict.items():
                    line = ''.join([key, ': ', value, ';\n'])
                    new_file.write(line)
            new_file.close()
        except Exception as e:
            raise UserError(_("Please follow the readme file. Contact to Administrator."
                              "\n %s") % e)

    @api.multi
    def set_customize_theme(self, company_id):
        try:
            if company_id:
                res_comp_id = self.env['res.company'].sudo().browse(company_id)
                if res_comp_id and res_comp_id.color:
                    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                    theme_path = path + "/web_theme_color/static/src/scss/variable.scss"
                    static_dict_theme.update({
                        '$o-enterprise-color': res_comp_id.color,
                    })
                    self.replace_file(theme_path, static_dict_theme)
        except Exception as e:
            raise UserError(_("Please Contact to Administrator. \n %s") % e)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
