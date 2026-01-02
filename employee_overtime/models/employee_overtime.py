from odoo import fields,models,api
from odoo.exceptions import AccessError, ValidationError

class EmployeeOvertime(models.Model):
    _name = 'employee.overtime'
    _description = 'A database/model for storing employee working hours over a specific period'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one(
        'employee.profile',
        'Employee',
        required=True,
        default=lambda self: self.env['employee.profile'].search([ ('user_id', '=', self.env.user.id) ], limit=1).id
    )
    date = fields.Date(string='Date', required=True, tracking=True)
    hours = fields.Float(string='Hours', required=True, tracking=True)
    reason = fields.Text(string='Reason')
    state = fields.Selection(
        [
            ('rejected', 'Rejected'),
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
        ],
        default = 'draft',
        tracking=True,
        string='Status'
    )

    def write(self, vals):
        if self.env.user.has_group('employee_overtime.group_overtime_employee'):

            for rec in self:
                if rec.state in ('submitted', 'approved', 'rejected') and 'state' not in vals:
                    raise AccessError("You cannot modify overtime after submission.")

                if rec.state == 'draft' and ( vals.get('state') in ('approved', 'rejected') ):
                    raise AccessError("Unauthorized action.")

                if rec.state == 'submitted' and ( vals.get('state') in ('draft', 'approved', 'rejected') ):
                    raise AccessError("Unauthorized action.")

                if rec.state == 'approved' and ( vals.get('state') in ('draft', 'submitted', 'rejected') ):
                    raise AccessError("Unauthorized action.")

                if rec.state == 'rejected' and ( vals.get('state') in ('draft', 'approved', 'submitted') ):
                    raise AccessError("Unauthorized action.")

        if self.env.user.has_group('employee_overtime.group_overtime_manager'):

            for rec in self:
                if rec.state in ('submitted', 'approved', 'rejected') and 'state' not in vals:
                    raise AccessError("You cannot modify overtime after submission.")

                if rec.state == 'draft' and ( vals.get('state') in ('approved', 'rejected') ):
                    raise AccessError("Draft overtime cannot be approved/rejected.")

                if ( rec.state in ('draft', 'approved', 'rejected') ) and vals.get('state') == 'submitted':
                    raise AccessError("Unauthorized action.")

                if ( rec.state in ('submitted', 'approved', 'rejected') ) and vals.get('state') == 'draft':
                    raise AccessError("Unauthorized action.")

        return super().write(vals)

    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise AccessError("You cannot delete overtime after submission.")
        return super().unlink()

    def action_submit(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError("Only draft overtime can be submitted.")
            rec.state = 'submitted'

    def action_approve(self):
        for rec in self:
            if rec.state != 'submitted':
                raise ValidationError("Only submitted overtime can be approved.")
            rec.state = 'approved'

    def action_reject(self):
        for rec in self:
            if rec.state != 'submitted':
                raise ValidationError("Only submitted overtime can be rejected.")
            rec.state = 'rejected'

    @api.constrains('hours')
    def _check_hours(self):
        for rec in self:
            if rec.hours <= 0 or rec.hours > 24:
                raise ValidationError("Overtime hours must be between 0 and 24.")

    @api.constrains('date')
    def _check_date(self):
        for rec in self:
            if rec.date < fields.Date.today():
                raise ValidationError("Overtime date cannot be in the past.")