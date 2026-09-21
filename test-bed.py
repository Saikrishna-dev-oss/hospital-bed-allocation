from models.bed import Bed

bed = Bed(
    bed_id="ICU-01",
    ward="ICU",
    bed_type="ICU",
    equipment="Ventilator",
    available=True
)

print("Bed ID:", bed.bed_id)
print("Ward:", bed.ward)
print("Bed Type:", bed.bed_type)
print("Equipment:", bed.equipment)
print("Available:", bed.available)