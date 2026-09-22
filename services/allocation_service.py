from csp.problem import HospitalBedCSP
from csp.propagation import propagate_domains
from csp.solver import solve_csp

def allocate_beds(patients, beds):
    # Create the CSP problem
    problem = HospitalBedCSP(patients, beds)

    # Propagate domains based on constraints
    propagate_domains(problem)

    # Solve the CSP
    solution = solve_csp(problem)
    if solution is None:
        return {
            "success": False,
            "allocation": {},
            "unallocated": [patient.patient_id for patient in patients]
        }

    allocated_patients = set(solution.keys())
    unallocated_patients = [patient.patient_id for patient in patients if patient.patient_id not in allocated_patients]

    return {
        "success": True,
        "allocation": solution,
        "unallocated": unallocated_patients
    }
