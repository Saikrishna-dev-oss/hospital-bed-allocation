from models.patient import Patient
from models.bed import Bed
from csp.constraints import check_bed_type, check_equipment, check_availability, check_isolation, is_valid_assignment

patient1 = Patient(patient_id="P001", bed_type_required="ICU", equipment_required="Ventilator", isolation_required=False)
patient2 = Patient("P002", "General", None, False)


bed1 = Bed("ICU-01", "ICU", "ICU", "Ventilator", True)
bed2 = Bed("ICU-02", "ICU", "ICU", None, False)
bed3 = Bed("GEN-01", "General", "General", None, True)

print("Bed Type Constraint:")
print("P001 + ICU-01:", check_bed_type(patient1, bed1))  # Expected: True
# print("P001 + ICU-02:", check_bed_type(patient1, bed2))  # Expected: True
print("P001 + GEN-01:", check_bed_type(patient1, bed3))  # Expected: False
print("P002 + ICU-01:", check_bed_type(patient2, bed1))  # Expected: False
print("P002 + ICU-02:", check_bed_type(patient2, bed2))  # Expected: False
print("P002 + GEN-01:", check_bed_type(patient2, bed3))  # Expected: True

print("\nEquipment Constraint:")
print("P001 + ICU-01:", check_equipment(patient1, bed1))
print("P001 + ICU-02:", check_equipment(patient1, bed2))
print("P002 + GEN-01:", check_equipment(patient2, bed3))

print("\nAvailability Constraint:")
print("P001 + ICU-01:", check_availability(bed1))  # Expected: True
print("P001 + ICU-02:", check_availability(bed2))  # Expected: False
print("P002 + GEN-01:", check_availability(bed3))  # Expected: True

print("\nIsolation Constraint:")
print("P001 + ICU-01:", check_isolation(patient1, bed1))  # Expected: True
print("P001 + ICU-02:", check_isolation(patient1, bed2))  # Expected: True
print("P002 + GEN-01:", check_isolation(patient2, bed3))  # Expected: True

print("\nOverall Valid Assignment:")
print("P001 + ICU-01:", is_valid_assignment(patient1, bed1)) #Expected: True
print("P001 + ICU-01:", is_valid_assignment(patient1, bed2)) #Expected: False
print("P001 + ICU-01:", is_valid_assignment(patient1, bed3)) #Expected: False
