from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, MedicationSKU

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Welcome to the Medication SKU Manager API!'

@app.route('/medications', methods=['POST'])
def create_medication():
    data = request.json

    # Validate data for non-empty, non-null, and non-whitespace values
    for key, value in data.items():
        if not value or isinstance(value, str) and value.isspace():
            return jsonify({"error": f"Field '{key}' cannot be empty, null, or whitespace."}), 400

    medication = MedicationSKU(
        medication_name=data['medication_name'],
        dose=data['dose'],
        presentation=data['presentation'],
        unit=data['unit'],
        countries=data['countries']
    )
    db.session.add(medication)
    db.session.commit()
    return jsonify({"message": "Medication created"}), 201

@app.route('/medications', methods=['GET'])
def get_medications():
    medications = MedicationSKU.query.all()
    return jsonify([med.to_dict() for med in medications]), 200

@app.route('/medications/<int:id>', methods=['PUT'])
def update_medication(id):
    data = request.json

    # Validate data for non-empty, non-null, and non-whitespace values
    for key, value in data.items():
        if not value or isinstance(value, str) and value.isspace():
            return jsonify({"error": f"Field '{key}' cannot be empty, null, or whitespace."}), 400

    medication = MedicationSKU.query.get_or_404(id)
    medication.medication_name = data['medication_name']
    medication.dose = data['dose']
    medication.presentation = data['presentation']
    medication.unit = data['unit']
    medication.countries = data['countries']
    db.session.commit()
    return jsonify({"message": "Medication updated"}), 200

@app.route('/medications/<int:id>', methods=['DELETE'])
def delete_medication(id):
    medication = MedicationSKU.query.get_or_404(id)
    db.session.delete(medication)
    db.session.commit()
    return jsonify({"message": "Medication deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)