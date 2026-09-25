# Hospital Bed Allocation Using CSP

A Constraint Satisfaction Problem (CSP)-based system that allocates available hospital beds to patients according to predefined requirements and constraints.

This project was developed as an Artificial Intelligence PBL project. It is a decision-support and resource-allocation prototype; it is **not** intended for medical diagnosis or real clinical decision-making.

---

## Project Overview

Hospitals have a limited number of beds, while patients may require particular bed types, equipment, isolation facilities, and availability. Manually assigning beds becomes difficult when several of these conditions must be satisfied at the same time.

This project models hospital bed allocation as a **Constraint Satisfaction Problem (CSP)**. It uses constraint checking, constraint propagation, and backtracking search to find a valid allocation of patients to available beds.

---

## Objectives

1. Model hospital bed allocation as a CSP.
2. Represent patients as CSP variables.
3. Generate compatible beds as the domain for each patient.
4. Eliminate invalid patient-bed assignments using constraints.
5. Use constraint propagation to reduce the search space.
6. Use backtracking search to find a valid complete allocation.
7. Display allocated and unallocated patients clearly.
8. Demonstrate a practical application of AI-based resource allocation.

---

## CSP Concepts Used

A Constraint Satisfaction Problem contains variables, domains, and constraints.

| CSP component | Project mapping |
| --- | --- |
| Variables | Patients, such as `P001`, `P002`, and `P003` |
| Domains | Beds that could potentially be assigned to each patient |
| Constraints | Rules that determine whether a patient-bed assignment is valid |
| Solution | A valid assignment of distinct beds to all patients, when one exists |

Example:

```text
P001 -> {ICU-01, ICU-02}
P002 -> {GEN-01, GEN-02}
```

### Implemented Constraints

The system checks the following conditions:

1. **Bed type compatibility** — a patient is assigned only a required bed type, such as ICU or General.
2. **Equipment compatibility** — a patient requiring equipment such as a ventilator is assigned only a bed that provides it.
3. **Bed availability** — unavailable beds cannot be assigned.
4. **Isolation compatibility** — a patient requiring isolation is assigned only an isolation-capable bed.
5. **One-bed-per-patient rule** — the same bed cannot be assigned to two patients.

---

## System Workflow

```text
User enters patients and beds
            |
            v
Patient and Bed objects are created
            |
            v
Allocation Service
            |
            v
CSP Problem: variables, domains, constraints
            |
            v
Constraint propagation
            |
            v
Backtracking solver
            |
            v
Allocation result shown in Streamlit UI
```

### Constraint Propagation

Constraint propagation removes choices that cannot remain valid after an assignment. For example:

```text
Before assignment:
P001 -> {B1}
P002 -> {B1, B2}

After P001 -> B1:
P002 -> {B2}
```

This reduces unnecessary search before or during solving.

### Backtracking Search

The solver starts with an empty assignment and tries compatible beds for each unassigned patient. If a choice leads to a conflict or dead end, it removes that choice and tries another one. It returns a complete valid allocation when one exists; otherwise, it reports that no complete allocation could be found.

---

## Architecture

```text
                    User
                     |
                     v
                Streamlit UI
                     |
                     v
          Patient / Bed Objects
                     |
                     v
            Allocation Service
                     |
                     v
                CSP Problem
          /          |          \
         v           v           v
  Constraints   Propagation    Solver
                                  |
                                  v
                           Backtracking
                                  |
                                  v
                         Valid Allocation
                                  |
                                  v
                            Streamlit UI
```

The application interface is separated from the CSP logic so that the allocation service, CSP problem, constraints, propagation, and solver can be tested independently.

---

## Features

### Patient Input

The application accepts:

- Patient ID
- Required bed type
- Required equipment
- Isolation requirement

### Bed Input

The application accepts:

- Bed ID
- Ward
- Bed type
- Equipment available at the bed
- Isolation status
- Availability status

### Allocation Results

When the user selects **Allocate Beds**, the application displays:

- Number of patients allocated
- Number of patients unallocated
- Patient-to-bed assignments
- Unallocated patients when a complete allocation is not possible

Example successful result:

```text
Patient P001 -> Bed ICU-02
Patient P002 -> Bed ICU-01
Patient P003 -> Bed GEN-01
```

---

## Technology Stack

| Area | Technology |
| --- | --- |
| Programming language | Python |
| User interface | Streamlit |
| AI technique | Constraint Satisfaction Problem (CSP) |
| Search | Backtracking Search |
| Search-space reduction | Constraint Propagation |
| Current data handling | In-memory Python objects |

The current version does **not** use SQLite or another database. Persistent storage is outside the implemented scope and is listed only as a future enhancement.

---

## Project Structure

```text
hospital-bed-allocation/
|
|-- assets/
|   `-- hospital_logo.png
|
|-- models/
|   |-- patient.py
|   |-- bed.py
|   `-- web.py
|
|-- csp/
|   |-- problem.py
|   |-- constraints.py
|   |-- propagation.py
|   `-- solver.py
|
|-- services/
|   `-- allocation_service.py
|
|-- app.py
|-- config.py
|-- requirements.txt
|-- README.md
|
|-- test-patient.py
|-- test-bed.py
|-- test-problem.py
|-- test-constraint.py
|-- test-propagation.py
|-- test-solver.py
|-- test-allocation.py
`-- test-noproblem.py
```

---

## Installation

1. Clone or download the project and open its root directory.
2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

From the project root, run:

```bash
streamlit run app.py
```

Streamlit will start the application and open it in a browser.

---

## Testing

The project includes component-level and end-to-end tests for:

- Patient model
- Bed model
- CSP problem representation
- Bed-type compatibility
- Equipment compatibility
- Isolation requirements
- Bed availability
- Constraint propagation
- Backtracking solver
- Allocation service
- Complete allocation and no-solution cases

The following professor demonstration cases have also been prepared for the Streamlit UI.

---

## Professor Demonstration Cases

### 1. Normal Allocation

```text
Patients:
P001 -> ICU
P002 -> General

Beds:
ICU-01 -> ICU, available
GEN-01 -> General, available
```

Expected: `P001 -> ICU-01` and `P002 -> GEN-01`.

### 2. Insufficient Suitable Beds

```text
Patients:
P001 -> ICU
P002 -> ICU
P003 -> ICU

Beds:
Fewer than three suitable, available ICU beds
```

Expected: no complete allocation is found.

### 3. Equipment Conflict

```text
Patients:
P001 -> ICU + Ventilator
P002 -> ICU
P003 -> General

Beds:
ICU-01 -> ICU, no equipment
ICU-02 -> ICU, ventilator
GEN-01 -> General
```

Expected: `P001 -> ICU-02`, `P002 -> ICU-01`, and `P003 -> GEN-01`.

### 4. Isolation Conflict

```text
Patients:
P001 -> ICU + isolation required
P002 -> ICU
P003 -> General

Beds:
ICU-01 -> ICU, not isolated
ICU-02 -> ICU, isolated
GEN-01 -> General
```

Expected: `P001 -> ICU-02`, `P002 -> ICU-01`, and `P003 -> GEN-01`.

### 5. Unavailable Bed

```text
Patients:
P001 -> ICU
P002 -> General

Beds:
ICU-01 -> ICU, unavailable
ICU-02 -> ICU, available
GEN-01 -> General, available
```

Expected: `P001 -> ICU-02` and `P002 -> GEN-01`. The unavailable ICU bed is ignored.

### 6. No Compatible Bed

```text
Patients:
P001 -> ICU + Ventilator
P002 -> General

Beds:
GEN-01 -> General
GEN-02 -> General
```

Expected: no complete allocation is found because P001 has no compatible bed.

### 7. Backtracking Demonstration

```text
Patients:
P001 -> ICU
P002 -> ICU + Ventilator
P003 -> General

Beds:
ICU-01 -> ICU + Ventilator
ICU-02 -> ICU, no equipment
GEN-01 -> General
```

Expected final allocation:

```text
P001 -> ICU-02
P002 -> ICU-01
P003 -> GEN-01
```

The first choice of `ICU-01` for P001 would leave P002 without its only compatible bed. The solver must backtrack and assign P001 to `ICU-02`.

### 8. Multiple Valid Beds

```text
Patients:
P001 -> ICU
P002 -> ICU
P003 -> General

Beds:
ICU-01 -> ICU
ICU-02 -> ICU
ICU-03 -> ICU
GEN-01 -> General
```

Expected: P001 and P002 receive different ICU beds, and P003 receives `GEN-01`. The exact valid ICU assignment may vary.

---

## Connection to the AI Syllabus

This project demonstrates core CSP concepts from the Artificial Intelligence syllabus.

| AI topic | Implementation in this project |
| --- | --- |
| Constraint Satisfaction Problems | Hospital bed allocation is formulated as a CSP |
| CSP definition | Patients are variables; compatible beds are domains; hospital requirements are constraints |
| Constraint propagation | Incompatible or already-used beds are removed from possible choices |
| Backtracking search | The solver explores assignments and undoes choices that lead to conflicts |
| Problem structure | Relationships among patients, beds, and requirements are modeled explicitly |

---

## Limitations

This is a simplified academic prototype. It does not currently include:

- Patient priority or triage handling
- Database or persistent storage
- Real-time bed availability updates
- Integration with hospital information systems
- Complex clinical rules or medical diagnosis
- Advanced optimization objectives
- Large-scale performance optimization
- Detailed reasons for every allocation conflict

---

## Future Enhancements

Possible future improvements include:

- Persistent storage using SQLite or another database
- Patient-priority handling
- Dynamic bed availability
- Support for additional wards and equipment types
- Allocation statistics and reports
- Detailed conflict explanations
- Local-search or optimization-based allocation strategies
- Visual representation of the CSP search process

These are not part of the current PBL implementation.

---

## Academic Scope

The project focuses on applying an AI problem-solving technique to a realistic resource-allocation scenario:

```text
Real-world allocation problem
            |
            v
CSP model: variables, domains, constraints
            |
            v
Constraint propagation
            |
            v
Backtracking search
            |
            v
Valid hospital-bed allocation
```

It should be presented as a CSP-based decision-support prototype, not as a replacement for hospital staff or clinical judgment.

---

## Project Status

| Component | Status |
| --- | --- |
| Project setup | Complete |
| Patient model | Complete |
| Bed model | Complete |
| CSP representation and domains | Complete |
| Constraints | Complete |
| Equipment, availability, and isolation rules | Complete |
| Constraint propagation | Complete |
| Backtracking solver | Complete |
| Allocation service | Complete |
| Streamlit UI | Complete |
| End-to-end allocation testing | Complete |
| Database persistence | Postponed / future enhancement |

---

## Conclusion

Hospital Bed Allocation Using CSP demonstrates how a real-world resource-allocation problem can be modeled with Constraint Satisfaction Problems. Patients are represented as variables, suitable beds form their domains, and hospital requirements are represented as constraints. Constraint propagation reduces invalid choices, while backtracking search finds a valid allocation when one exists.

The project provides a clear academic demonstration of CSP modeling, constraint checking, propagation, and backtracking in a practical hospital-bed allocation scenario.
