from odoo import models, fields, api


class MedicalPrescription(models.Model):
    _name = 'medical.prescription'
    _description = 'Medical Prescription'

    name = fields.Char(string='Prescription Reference', required=True, copy=False, readonly=True, default='New')
    patient_id = fields.Many2one('res.partner', string='Patient', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor', required=True)
    appointment_id = fields.Many2one('medical.appointment', string='Appointment')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    
    line_ids = fields.One2many('medical.prescription.line', 'prescription_id', string='Prescription Lines')

