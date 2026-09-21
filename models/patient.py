class Patient:
    def __init__(self, patient_id, bed_type_required, isolation_required=False, equipment_required=None):
        self.patient_id = patient_id
        self.bed_type_required = bed_type_required
        self.isolation_required = isolation_required
        self.equipment_required = equipment_required
