# -*- coding: utf-8 -*-
from odoo import models, fields, api
from openerp.tools.translate import _

class EmployeeInherite(models.Model):
    _inherit = 'hr.employee'
    _description = "Generate employee id"

    emp_id = fields.Char(string="Employee Id",required=True, readonly=True, index=True, default= lambda self: _('New'))
    # emp_id = fields.Char(string="Employee Id",required=True, readonly=True, index=True, default='New')

    @api.model
    def create(self, values):
        if values.get('emp_id', _('New')) == _('New'):
            values['emp_id'] = self.env['ir.sequence'].next_by_code('dsl.employee.sequence') or _('New')
        result = super(EmployeeInherite, self).create(values)
        return result



