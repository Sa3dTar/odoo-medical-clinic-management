from odoo import models, fields, api


class MedicalPrescriptionLine(models.Model):
    _name = 'medical.prescription.line'
    _description = 'Prescription Line'

    prescription_id = fields.Many2one('medical.prescription', string='Prescription', required=True, onDelete='cascade')
    medicine_name = fields.Char(string='Medicine Name', required=True)
    dose = fields.Char(string='Dose (e.g., 1 tablet)', required=True)
    frequency = fields.Char(string='Frequency (e.g., 3 times daily)', required=True)
    duration = fields.Char(string='Duration (e.g., 5 days)', required=True)
    instructions = fields.Text(string='Additional Instructions')