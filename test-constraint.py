from models.patient import Patient
from models.bed import Bed
from csp.constraints import check_bed_type
patient1 = Patient("P001", "ICU", False, "Ventilator")
patient2 = Patient("P002", "General", False, None)


bed1 = Bed("ICU-01", "ICU", "ICU", "Ventilator", True)
bed2 = Bed("ICU-02", "ICU", "ICU", None, True)
bed3 = Bed("GEN-01", "General", "General", None, True)

print("P001 + ICU-01:", check_bed_type(patient1, bed1))  # Expected: True
# print("P001 + ICU-02:", check_bed_type(patient1, bed2))  # Expected: True
print("P001 + GEN-01:", check_bed_type(patient1, bed3))  # Expected: False

print("P002 + ICU-01:", check_bed_type(patient2, bed1))  # Expected: False
print("P002 + ICU-02:", check_bed_type(patient2, bed2))  # Expected: False
print("P002 + GEN-01:", check_bed_type(patient2, bed3))  # Expected: True