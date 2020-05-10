# -*- coding: utf-8 -*-
from odoo import models, fields, api
from openerp.tools.translate import _

class EmployeeInherite(models.Model):
    _inherit = 'hr.employee'
    _description = "Generate employee id"
    _rec_name = 'employee_id'

    employee_id = fields.Char(string="Employee Id",required=False, index=True, default= lambda self: _(''))
    # emp_id = fields.Char(string="Employee Id",required=True, readonly=True, index=True, default='New')

    @api.model
    def create(self, values):
        cr, context = self._cr, self._context

        if values.get('employee_id', _('')) != _(''):
            result = super(EmployeeInherite, self).create(values)
            return result
            # values['emp_id'] = self.env['ir.sequence'].with_context(force_company=values['company_id']).next_by_code('dsl.employee.sequence') or _('')
        company_id = values.get('company_id')
        if not values.get('company_id'):
            company_id = 1
        company = self.env['res.company'].browse(company_id)
        # values['emp_id'] = str(company.employee_id_code) + str(values['emp_id'])

        cr.execute(""" select employee_id from hr_employee where company_id = '""" + str(company.id) + """'
        order by id  desc limit 1        """)
        rec = cr.fetchone()

        if rec:
            cnum = str(rec[0])
            if len(cnum) > 2:
                cnum = cnum[2:]
            else:
                cnum = '0'
            emp_id = int(cnum) + 1
            values['employee_id'] = str(company.employee_id_code) + str(emp_id).zfill(7)
        else:
            values['employee_id'] = str(company.employee_id_code) + str('1').zfill(7)
        result = super(EmployeeInherite, self).create(values)
        return result



