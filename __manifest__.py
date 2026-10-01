{
    'name': 'Medical Clinic & Hospital Management',
    'version': '18.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'Integrated Medical Clinic Management System with Appointments, EMR, Prescriptions, and Commission Billing',
    'author': 'Saad Tarek',
    'depends': ['base', 'mail', 'account'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data / Sequences
        'data/sequence.xml',
        
        # Views
        'views/medical_appointment.xml',
        'views/medical_record.xml',
        'views/medical_prescription.xml',
        'views/medical_doctor_commision.xml',
        'views/menuitems.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}