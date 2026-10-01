from odoo import models, fields, api

class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Medical Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain=[('is_patient', '=', '=', True)])
    doctor_id = fields.Many2one('res.users', string='Doctor', required=True, domain=[('share', '=', False)])
    appointment_date = fields.Datetime(string='Appointment Date & Time', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    
    # ربط الموعد بالروشتة والفاتورة
    prescription_id = fields.Many2one('medical.prescription', string='Prescription', readonly=True)
    invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True)
    consultation_fee = fields.Float(string='Consultation Fee', required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or _('New')
        return super().create(vals)