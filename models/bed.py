class Bed:
    def __init__(self, bed_id, ward, bed_type, equipment=None, available=True):
        self.bed_id = bed_id
        self.ward = ward
        self.bed_type = bed_type
        self.equipment = equipment
        self.available = available
    