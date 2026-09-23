CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    bed_type_required TEXT NOT NULL,
    equipment_required TEXT,
    isolation_required INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS beds (
    bed_id TEXT PRIMARY KEY,
    ward TEXT NOT NULL,
    bed_type TEXT NOT NULL,
    equipment TEXT,
    available INTEGER NOT NULL,
    isolation INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS allocations (
    allocation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT NOT NULL,
    bed_id TEXT NOT NULL,
    allocated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (bed_id) REFERENCES beds(bed_id)
);