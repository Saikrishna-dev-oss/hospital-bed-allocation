# Hospital Bed Allocation Using CSP — Project Progress

## 1. Project Goal

Build a college PBL project called **Hospital Bed Allocation Using CSP**.

The system will allocate available hospital beds to patients based on predefined requirements and constraints.

This is a **Constraint Satisfaction Problem (CSP)** project.

The system is a decision-support/resource-allocation prototype. It is **not** intended to make medical diagnoses or clinical decisions.

---

## 2. Learning Approach

The project is being developed **one step at a time**.

The user wants to understand:

* Why each component exists
* How the algorithm works
* How the Python code implements the algorithm
* How the different files communicate
* How the CSP concepts map to the real hospital problem

Do **not** jump directly to the final implementation.

For every step:

1. Explain the concept.
2. Explain why we need it.
3. Create one file/component.
4. Explain the code.
5. Test it.
6. Confirm it works.
7. Update this progress document.
8. Only then move to the next step.

---

# 3. Technology Stack

Current planned stack:

* Python
* Streamlit
* SQLite

The important AI logic will be implemented ourselves rather than using an external AI/ML model.

Current `requirements.txt` contains:

```text
streamlit
```

No other dependency has been added yet.

---

# 4. Core AI Concept

The project uses a **Constraint Satisfaction Problem (CSP)**.

A CSP consists of:

### Variables

Each **patient** is a CSP variable.

Example:

```text
P001
P002
P003
```

### Domains

The domain of a patient is the set of beds that could potentially be assigned to that patient.

Example:

```text
P001 → {ICU-01, ICU-02}
```

### Constraints

Rules determine whether a patient-bed assignment is valid.

Current core constraints:

1. Bed type compatibility
2. Equipment compatibility
3. Bed availability
4. One bed can be assigned to only one patient
5. Isolation requirement

---

# 5. Important CSP Concepts Already Learned

## Constraint Propagation

When a bed becomes unavailable because it was assigned to another patient, that bed is removed from other patients' domains.

Example:

```text
Before:

P001 → {B1}
P002 → {B1, B2}

P001 → B1

After propagation:

P002 → {B2}
```

Constraint propagation reduces impossible choices.

---

## Backtracking

If the solver makes a choice and later reaches a conflict, it goes back to an earlier decision and tries another possible value.

Conceptually:

```text
Choose
  ↓
Assign
  ↓
Propagate
  ↓
Continue
  ↓
Conflict
  ↓
Backtrack
  ↓
Try another choice
```

---

## Empty Domain

If a patient's domain becomes:

```text
P003 → {}
```

there is no valid bed remaining for that patient under the current assignments.

The solver must backtrack if alternatives exist.

If no alternative can produce a solution, the system reports that a complete allocation is not possible.

---

# 6. Initial Hospital Data Model

## Patient

Current planned patient information:

```text
Patient
├── patient_id
├── bed_type_required
├── isolation_required
└── equipment_required
```

Optional fields such as age and priority may be considered later.

---

## Bed

Current planned bed information:

```text
Bed
├── bed_id
├── ward
├── bed_type
├── equipment
└── available
```

---

# 7. Agreed Project Structure

```text
hospital-bed-allocation/
│
├── app.py
├── config.py
│
├── database/
│   ├── db.py
│   └── schema.sql
│
├── models/
│   ├── patient.py
│   ├── bed.py
│   └── allocation.py
│
├── csp/
│   ├── problem.py
│   ├── constraints.py
│   ├── propagation.py
│   └── solver.py
│
├── services/
│   ├── patient_service.py
│   ├── bed_service.py
│   └── allocation_service.py
│
├── ui/
│   ├── dashboard.py
│   ├── patient_ui.py
│   ├── bed_ui.py
│   └── results_ui.py
│
├── utils/
│   └── helpers.py
│
├── data/
│   └── hospital.db
│
├── PROJECT_PROGRESS.md
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 8. Architecture

The overall flow will eventually be:

```text
                    USER
                     │
                     ▼
               Streamlit UI
                     │
                     ▼
                 Services
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Database              CSP Engine
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 Problem   Propagation   Solver
                                │
                                ▼
                         Valid Allocation
                                │
                                ▼
                           Save Result
                                │
                                ▼
                                UI
```

The CSP engine should remain independent from Streamlit.

The goal is eventually to be able to conceptually do:

```python
solution = solve_csp(patients, beds)
```

and receive an allocation result.

---

# 9. Development Phases

## Phase 1 — Foundation

* Project setup
* Virtual environment
* Requirements
* Models
* Database

## Phase 2 — CSP Engine

* Represent CSP
* Generate patient domains
* Implement constraints
* Implement constraint propagation
* Implement backtracking search
* Later consider MRV heuristic

## Phase 3 — Application Layer

* Services
* Connect database to CSP
* Connect CSP to UI

## Phase 4 — User Interface

* Dashboard
* Patient input
* Bed input
* Allocation results
* Conflict/no-solution display

## Phase 5 — Testing

Test:

* Normal allocation
* Multiple possible beds
* Occupied beds
* Equipment conflicts
* Isolation conflicts
* Insufficient beds
* No complete solution
* Multiple valid solutions

## Phase 6 — Documentation and Presentation

* README
* Architecture explanation
* Algorithm explanation
* Screenshots
* PBL presentation
* Viva preparation

---

# 10. CURRENT PROJECT PROGRESS

## Completed

### Project setup

* [x] Project folder created
* [x] Project structure created
* [x] Virtual environment created
* [x] `requirements.txt` created
* [x] Streamlit added to `requirements.txt`

### CSP understanding

* [x] Understood CSP
* [x] Understood variables
* [x] Understood domains
* [x] Understood constraints
* [x] Understood constraint propagation
* [x] Understood backtracking
* [x] Understood empty domains/conflicts
* [x] Manually walked through CSP allocation examples

### Patient model

File:

```text
models/patient.py
```

Current code:

```python
class Patient:
    def __init__(
        self,
        patient_id,
        bed_type_required,
        isolation_required=False,
        equipment_required=None
    ):
        self.patient_id = patient_id
        self.bed_type_required = bed_type_required
        self.isolation_required = isolation_required
        self.equipment_required = equipment_required
```

Patient model has been successfully tested.

Temporary `test_patient.py` was used for verification.

Expected successful output included:

```text
Patient ID: P001
Bed Type: ICU
Isolation: False
Equipment: Ventilator
```

---

# 11. CURRENT STEP

We are currently implementing:

```text
models/bed.py
```

The Bed model has already been explained.

Planned code:

```python
class Bed:
    def __init__(
        self,
        bed_id,
        ward,
        bed_type,
        equipment=None,
        available=True
    ):
        self.bed_id = bed_id
        self.ward = ward
        self.bed_type = bed_type
        self.equipment = equipment
        self.available = available
```

A temporary `test_bed.py` should be used to verify it.

Expected test data:

```text
Bed ID: ICU-01
Ward: ICU
Bed Type: ICU
Equipment: Ventilator
Available: True
```

---

# 12. EXACT NEXT STEP

After `models/bed.py` is tested successfully:

DO NOT immediately create more files.

First explain:

```text
Patient Object
       +
Bed Object
       ↓
CSP representation
       ↓
Variables
       +
Domains
```

The next conceptual goal is to understand exactly how the normal Python objects become the mathematical CSP representation.

After that, continue one file at a time.

---

# 13. Important Development Rules

* Do not skip explanations.
* Do not dump the entire project code at once.
* Do not jump ahead several files.
* Explain each file before creating it.
* Test each component before moving forward.
* Keep the CSP logic separate from the UI.
* Keep the implementation understandable enough for a college viva.
* Prefer implementing the CSP logic ourselves rather than hiding it behind a library.
* Do not add unnecessary AI/ML features that are outside the project's CSP scope.
* Keep the first version simple and working before adding enhancements.

---

# 14. How to Continue in a New Chat

If the conversation reaches its limit:

1. Start a new chat.
2. Upload this `PROJECT_PROGRESS.md`.
3. Say:

"Continue the Hospital Bed Allocation CSP project using the uploaded PROJECT_PROGRESS.md. Start exactly from the CURRENT STEP. Do not restart or skip ahead."

The uploaded progress document should be treated as the primary project handoff document.

The actual project files remain the source of truth for the code.
This document is the source of truth for project progress, decisions, learning state, and the next step.
