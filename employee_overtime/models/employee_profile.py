from odoo import fields,models

class EmployeeProfile(models.Model):
    _name = 'employee.profile'
    _description = 'A database/model storing employee info'

    name = fields.Char(string="Employee Name", required=True)
    job_title = fields.Char(string="Job Title", required=True)
    work_email = fields.Char(string="Work Email", required=True)
    work_phone = fields.Char(string="Work Phone", required=True)

    user_id = fields.Many2one('res.users', string="Related User", ondelete='set null', index=True)

    _sql_constraints = [
        ('unique_user', 'unique(user_id)', 'Each user can be linked to at most one employee record.'),
    ]