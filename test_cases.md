```
Patient ID: P001
Bed Type Required: ICU
Equipment Required: None
Isolation Required: No

Patient ID: P002
Bed Type Required: General
Equipment Required: None
Isolation Required: No
```
```
Bed ID: ICU-01
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No


Bed ID: GEN-01
Ward: General
Bed Type: General
Equipment: None
Available: Yes
Isolation: No
```
---
## Test Case 2 - Impossible AllocationP001 → ICU

P002 → ICU
P003 → ICU

Equipment: None
Isolation: No


ICU-01 → ICU → Available
ICU-02 → ICU → Available

---

# Equpiment Conflict
```
Number of Patients: 3

Patient 1:
Patient ID: P001
Bed Type Required: ICU
Equipment Required: Ventilator
Isolation Required: No

Patient 2:
Patient ID: P002
Bed Type Required: ICU
Equipment Required: None
Isolation Required: No

Patient 3:
Patient ID: P003
Bed Type Required: General
Equipment Required: None
Isolation Required: No


Number of Beds: 3

Bed 1:
Bed ID: ICU-01
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No

Bed 2:
Bed ID: ICU-02
Ward: ICU
Bed Type: ICU
Equipment: Ventilator
Available: Yes
Isolation: No

Bed 3:
Bed ID: GEN-01
Ward: General
Bed Type: General   
Equipment: None
Available: Yes
Isolation: No
```
# Islation Conflict
```
Number of Patients: 3

Patient 1:
Patient ID: P001
Bed Type Required: ICU
Equipment Required: None
Isolation Required: Yes

Patient 2:
Patient ID: P002
Bed Type Required: ICU
Equipment Required: None
Isolation Required: No

Patient 3:
Patient ID: P003
Bed Type Required: General
Equipment Required: None
Isolation Required: No


Number of Beds: 3

Bed 1:
Bed ID: ICU-01
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No

Bed 2:
Bed ID: ICU-02
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: Yes

Bed 3:
Bed ID: GEN-01
Ward: General
Bed Type: General
Equipment: None
Available: Yes
Isolation: No
```
# Back Tracking
```
Number of Patients: 3

Patient 1:
Patient ID: P001
Bed Type Required: ICU
Equipment Required: None
Isolation Required: No

Patient 2:
Patient ID: P002
Bed Type Required: ICU
Equipment Required: Ventilator
Isolation Required: No

Patient 3:
Patient ID: P003
Bed Type Required: General
Equipment Required: None
Isolation Required: No

Number of Beds: 3

Bed 1:
Bed ID: ICU-01
Ward: ICU
Bed Type: ICU
Equipment: Ventilator
Available: Yes
Isolation: No

Bed 2:
Bed ID: ICU-02
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No

Bed 3:
Bed ID: GEN-01
Ward: General
Bed Type: General
Equipment: None
Available: Yes
Isolation: No
```

# Multiple Valid Beds
```
Number of Patients: 3

Patient 1:
Patient ID: P001
Bed Type Required: ICU
Equipment Required: None
Isolation Required: No

Patient 2:
Patient ID: P002
Bed Type Required: ICU
Equipment Required: None
Isolation Required: No

Patient 3:
Patient ID: P003
Bed Type Required: General
Equipment Required: None
Isolation Required: No

Number of Beds: 4

Bed 1:
Bed ID: ICU-01
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No

Bed 2:
Bed ID: ICU-02
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No

Bed 3:
Bed ID: ICU-03
Ward: ICU
Bed Type: ICU
Equipment: None
Available: Yes
Isolation: No

Bed 4:
Bed ID: GEN-01
Ward: General
Bed Type: General
Equipment: None
Available: Yes
Isolation: No
```
