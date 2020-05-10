# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CompanyInherit(models.Model):
    _inherit = 'res.company'
    _description = "Employee ID Code"
    employee_id_code = fields.Char("Employee ID Code")
