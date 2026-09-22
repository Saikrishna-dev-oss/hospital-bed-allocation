def check_bed_type(patient, bed):
    """
    Check if the bed type is suitable for the patient.
    """
    return patient.bed_type_required == bed.bed_type

def check_equipment(patient, bed):
    """
    Check if the bed has the required equipment for the patient.
    """
    if patient.equipment_required is None:
        return True  
    
    return patient.equipment_required == bed.equipment

def check_availability(bed):
    """
    Check if the bed is available for the patient.
    """
    return bed.available

def check_isolation(patient, bed):
    """
    Check if the bed is suitable for isolation requirements.
    """
    if not patient.isolation_required:
        return True  # If the patient does not require isolation, any bed is suitable
    return bed.isolation # If the patient requires isolation, the bed must be in an isolation ward

def is_valid_assignment(patient, bed):
    """
    Check if the assignment of a patient to a bed is valid based on all constraints.
    """
    return (
        check_bed_type(patient, bed) and
        check_equipment(patient, bed) and
        check_availability(bed) and
        check_isolation(patient, bed)
        )
