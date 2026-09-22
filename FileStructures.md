## Project Structure
The project is organized into several directories and files, each serving a specific purpose in the Hospital Bed Allocation CSP project. Below is an overview of the project structure:

```
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
├── requirements.txt
├── README.md
└── .gitignore
```

## Patient Structure\
```
Patient
│
├── patient_id
├── bed_type_required
├── isolation_required
└── equipment_required
```

```
Bed
│
├── bed_id
├── ward
├── bed_type
├── equipment
└── available
```

```
                 Hospital Data
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      Patients                  Beds
          │                       │
          ▼                       ▼
      Variables             Possible Values
          │                       │
          └───────────┬───────────┘
                      ▼
                Apply Constraints
                      │
                      ▼
                  Domains
                      │
                      ▼
             Constraint Propagation
                      │
                      ▼
                Backtracking
                      │
                      ▼
                  Solution
```

## CSP Folder Flow
```
Patient objects ─────┐
                     │
                     ▼
                problem.py
                     │
                     ▼
               CSP Variables
                     +
                  Domains
                     │
                     ▼
              constraints.py
                     │
                     ▼
            Valid / Invalid choices
                     │
                     ▼
              propagation.py
                     │
                     ▼
             Reduced domains
                     │
                     ▼
                solver.py
                     │
                     ▼
              Final allocation
```

After Propagation

```
Patient + Beds
       ↓
   problem.py
       ↓
Variables + Domains
       ↓
 constraints.py
       ↓
Check constraints
       ↓
propagation.py
       ↓
Remove invalid values
       ↓
   Reduced domains
       ↓
     solver.py
       ↓
 Backtracking Search
       ↓
 Final Allocation
 ```
 