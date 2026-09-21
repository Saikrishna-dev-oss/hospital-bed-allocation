def check_bed_type(patient, bed):
    """
    Check if the bed type is suitable for the patient.
    """
    return patient.bed_type_required == bed.bed_type
