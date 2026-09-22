from csp.constraints import is_valid_assignment

def solve_csp(problem):

    """
    Solve the CSP using backtracking search.
    """
    assignment = {}
    return backtrack(problem, assignment)

def backtrack(problem, assignment):

    if len(assignment) == len(problem.patients):
        return assignment.copy()

    patient = None
    for p in problem.patients:
        if p.patient_id not in assignment:
            patient = p
            break

    if patient is None:
        return None

    for bed_id in problem.domains[patient.patient_id]:
        if bed_id in assignment.values():
            continue

        bed = None

        for b in problem.beds:
            if b.bed_id == bed_id:
                bed = b
                break

        if not is_valid_assignment(patient, bed):
            continue

        assignment[patient.patient_id] = bed_id

        result = backtrack(problem, assignment)
        if result is not None:
            return result

        del assignment[patient.patient_id]

    return None