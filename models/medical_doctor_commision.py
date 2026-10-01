from odoo import models, fields, api

class MedicalDoctorCommission(models.Model):
    _name = 'medical.doctor.commission'
    _description = 'Doctor Commission Management'

    doctor_id = fields.Many2one('res.users', string='Doctor', required=True)
    appointment_id = fields.Many2one('medical.appointment', string='Appointment', required=True)
    invoice_id = fields.Many2one('account.move', string='Customer Invoice', required=True)
    
    # التصحيح هنا: استخدام Monetary بدلاً من Float ليتوافق مع amount_total في الفواتير
    currency_id = fields.Many2one('res.currency', related='invoice_id.currency_id', store=True, readonly=True)
    total_amount = fields.Monetary(string='Consultation Amount', related='invoice_id.amount_total', store=True, currency_field='currency_id')
    
    commission_percentage = fields.Float(string='Commission Percentage (%)', default=50.0)
    commission_amount = fields.Monetary(string='Doctor Commission', compute='_compute_commission', store=True, currency_field='currency_id')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('paid', 'Paid')
    ], string='Status', default='draft')

    @api.depends('total_amount', 'commission_percentage')
    def _compute_commission(self):
        for record in self:
            record.commission_amount = (record.total_amount * record.commission_percentage) / 100.0