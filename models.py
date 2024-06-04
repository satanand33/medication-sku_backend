# backend/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MedicationSKU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medication_name = db.Column(db.String(100), nullable=False)
    dose = db.Column(db.String(50), nullable=False)
    presentation = db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    countries = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'medication_name': self.medication_name,
            'dose': self.dose,
            'presentation': self.presentation,
            'unit': self.unit,
            'countries': self.countries
        }
