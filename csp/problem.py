class HospitalBedCSP:

    def __init__(self, patients, beds):
        self.patients = patients
        self.beds = beds

        self.variables = [patient.patient_id for patient in self.patients]

        self.domains = {patient.patient_id :[bed.bed_id for bed in self.beds] for patient in self.patients}

    