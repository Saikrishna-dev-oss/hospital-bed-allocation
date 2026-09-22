
from models.patient import Patient
from models.bed import Bed
from services.allocation_service import allocate_beds
patient1 = Patient("P001", "ICU", "ventilator", False)
patient2 = Patient("P002", "General", None, False)
patient3 = Patient("P003", "ICU", None, False)

bed1 = Bed("ICU-01", "ICU", "ICU", "ventilator", True)
bed2 = Bed("ICU-02", "ICU", "ICU", "ventilator", True)
bed3 = Bed("ICU-03", "ICU", "ICU", None, True)
bed4 = Bed("GEN-01", "General", "General", None, True)

patients = [patient1, patient2, patient3]
beds = [bed1, bed2, bed3, bed4]

allocation = allocate_beds(patients, beds)
if allocation:
    print("Allocation successful:")
    for patient_id, bed_id in allocation.items():
        print(f"Patient {patient_id} -> Bed {bed_id}")
else:
    print("No valid allocation found.")
