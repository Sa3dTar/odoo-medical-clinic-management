from odoo import models, fields, api


class MedicalRecord(models.Model):
    _name = 'medical.record'
    _description = 'Electronic Medical Record (EMR)'

    patient_id = fields.Many2one('res.partner', string='Patient', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor', required=True)
    appointment_id = fields.Many2one('medical.appointment', string='Appointment')
    visit_date = fields.Datetime(string='Visit Date', default=fields.Datetime.now)
    
    # العلامات الحيوية والتشخيص
    blood_pressure = fields.Char(string='Blood Pressure')
    heart_rate = fields.Char(string='Heart Rate')
    temperature = fields.Float(string='Temperature (°C)')
    weight = fields.Float(string='Weight (kg)')
    
    diagnosis = fields.Text(string='Diagnosis / Notes', required=True)