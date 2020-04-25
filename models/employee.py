# -*- coding: utf-8 -*-
from odoo import models, fields, api
from openerp.tools.translate import _

class EmployeeInherite(models.Model):
    _inherit = 'hr.employee'
    _description = "Generate employee id"

    emp_id = fields.Char(string="Employee Id",required=False, index=True, default= lambda self: _(''))
    # emp_id = fields.Char(string="Employee Id",required=True, readonly=True, index=True, default='New')

    @api.model
    def create(self, values):
        cr, context = self._cr, self._context

        # if values.get('emp_id', _('')) == _(''):
            # values['emp_id'] = self.env['ir.sequence'].with_context(force_company=values['company_id']).next_by_code('dsl.employee.sequence') or _('')
        company = self.env['res.company'].browse(values.get('company_id'))
        # values['emp_id'] = str(company.employee_id_code) + str(values['emp_id'])

        cr.execute(""" select emp_id from hr_employee where company_id = '""" + str(values.get('company_id')) + """'
        order by id  desc limit 1        """)
        rec = cr.fetchone()

        if rec:
            cnum = str(rec[0])
            if len(cnum) > 2:
                cnum = cnum[2:]
            else:
                cnum = '0'
            values['emp_id'] = str(company.employee_id_code) + str(int(cnum) + 1).zfill(7)
        else:
            values['emp_id'] = str(company.employee_id_code) + str('1').zfill(7)
        result = super(EmployeeInherite, self).create(values)
        return result



