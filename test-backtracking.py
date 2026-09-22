from models.patient import Patient
from models.bed import Bed
from csp.problem import HospitalBedCSP
from csp.propagation import propagate_domains
from csp.solver import solve_csp

# -------------------------
# Patients
# -------------------------

patient1 = Patient(
    "P001",
    "ICU",
    None,
    False
)

patient2 = Patient(
    "P002",
    "ICU",
    "ventilator",
    False
)


# -------------------------
# Beds
# -------------------------

bed1 = Bed(
    "ICU-01",
    "ICU",
    "ICU",
    "ventilator",
    True
)

bed2 = Bed(
    "ICU-02",
    "ICU",
    "ICU",
    None,
    True
)


patients = [patient1, patient2]
beds = [bed1, bed2]


# -------------------------
# Create CSP
# -------------------------

problem = HospitalBedCSP(patients, beds)


# -------------------------
# Propagation
# -------------------------

propagate_domains(problem)

print("Domains after propagation:")

for patient_id, domain in problem.domains.items():
    print(f"{patient_id} -> {domain}")


# -------------------------
# Solve
# -------------------------

print("\nSolving...")

solution = solve_csp(problem)


# -------------------------
# Result
# -------------------------

if solution:
    print("\nSolution found:")

    for patient_id, bed_id in solution.items():
        print(f"{patient_id} -> {bed_id}")

else:
    print("\nNo solution found.")