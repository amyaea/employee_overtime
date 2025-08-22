from odoo import api,fields,models
from datetime import date, timedelta

class EmployeeOvertime(models.Model):
    _name = 'hr.overtime'
    _description = 'A database/model for storing employee working hours over a specific period'

    def _default_employee(self):
        return self.env['hr.employee.details'].search([('user_id', '=', self.env.user.id)], limit=1).id

    employee_id = fields.Many2one(
        'hr.employee.details',
        'Employee',
        required=True,
        default=_default_employee,
    )
    date = fields.Date(string='Date', required=True)
    hours = fields.Float(string='Hours', required=True)
    reason = fields.Text(string='Reason')
    state = fields.Selection(
        [
            ('rejected', 'Rejected'),
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
        ],
        default = 'draft',
        string='Status'
    )

    is_today = fields.Boolean(compute="_compute_is_today", store=True)
    is_tomorrow = fields.Boolean( compute="_compute_is_tomorrow", store=True)
    is_next_week = fields.Boolean(compute="_compute_is_next_week", store=True)
    is_next_month = fields.Boolean(compute="_compute_is_next_month", store=True)

    def action_submit(self):
        for rec in self:
            rec.state = 'submitted'

    def action_approve(self):
        for rec in self:
            rec.state = 'approved'

    def action_reject(self):
        for rec in self:
            rec.state = 'rejected'

    @api.depends('date')
    def _compute_is_today(self):
        today= date.today()
        for record in self:
            record.is_today = record.date == today

    @api.depends('date')
    def _compute_is_tomorrow(self):
        tomorrow = date.today() + timedelta(days=1)
        for record in self:
            record.is_tomorrow = record.date == tomorrow

    @api.depends('date')
    def _compute_is_next_week(self):
        next_week = date.today() + timedelta(days=7)
        for record in self:
            record.is_next_week = record.date == next_week

    @api.depends('date')
    def _compute_is_next_month(self):
        next_month = date.today() + timedelta(days=30)
        for record in self:
            record.is_next_month = record.date == next_month