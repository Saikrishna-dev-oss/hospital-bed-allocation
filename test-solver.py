from models.patient import Patient
from models.bed import Bed
from csp.problem import HospitalBedCSP
from csp.propagation import propagate_domains
from csp.solver import solve_csp

patient1 = Patient("P001", "ICU", "ventilator", False)
patient2 = Patient("P002", "General", None, False)
patient3 = Patient("P003", "ICU", None, False)

bed1 = Bed("ICU-01", "ICU", "ICU", "ventilator", True)
bed2 = Bed("ICU-02", "ICU", "ICU", "ventilator", True)
bed3 = Bed("ICU-03", "ICU", "ICU", None, True)
bed4 = Bed("GEN-01", "General", "General", None, True)

patients = [patient1, patient2, patient3]
beds = [bed1, bed2, bed3, bed4]

problem = HospitalBedCSP(patients, beds)

print("\nVariables (Patient IDs):")
print(*problem.variables, "\n")
for patient_id in problem.variables:
    print(f"Patient {patient_id} -> Domain: {problem.domains[patient_id]}")

print("\nPropagated Domains:")
propagate_domains(problem)
for patient_id in problem.variables:
    print(f"Patient {patient_id} -> Domain: {problem.domains[patient_id]}")

print("\nsolving the problem")
solution = solve_csp(problem)

if solution:
    for patient_id, bed_id in solution.items():
        print(f"Patient {patient_id} -> {bed_id}")
else:
    print("No solution found.")