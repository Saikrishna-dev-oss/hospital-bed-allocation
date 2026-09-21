from models.patient import Patient

patient = Patient("P001", "ICU",False,"Ventilator")

print("Patient ID:", patient.patient_id)
print("Bed Type:", patient.bed_type_required)
print("Isolation:", patient.isolation_required)
print("Equipment:", patient.equipment_required)