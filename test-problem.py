from models.patient import Patient
from models.bed import Bed
from csp.problem import HospitalBedCSP

patient1 = Patient("P001", "ICU", False, "ventilator")
patient2 = Patient("P002", "General", False, None)

bed1 = Bed("ICU-01", "ICU", "ICU", "ventilator", True)
bed2 = Bed("ICU-02", "ICU", "ICU", None, True)
bed3 = Bed("GEN-01", "General", "General", None, True)


patients = [patient1, patient2]
beds = [bed1, bed2, bed3]

problem = HospitalBedCSP(patients, beds)

print("\nVariables (Patient IDs):")
print(*problem.variables)

print("\nDomains (Available Beds for Each Patient):")
for patient_id, domain in problem.domains.items():
    print(f"Patient {patient_id} -> {domain}")