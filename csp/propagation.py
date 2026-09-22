from csp.constraints import is_valid_assignment

def propagate_domains(problem):
    """
    Propagate the domains of the CSP based on the constraints.
    This function modifies the domains in place.
    """

    for patient in problem.patients:
        valid_beds = []

        for bed in problem.beds:
            if is_valid_assignment(patient, bed):
                valid_beds.append(bed.bed_id)
        problem.domains[patient.patient_id] = valid_beds

    return problem.domains