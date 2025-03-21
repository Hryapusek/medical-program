CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT
);

CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    office_number VARCHAR(50)
);

CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id) ON DELETE CASCADE,
    doctor_id INT REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    appointment_date TIMESTAMPTZ NOT NULL,
    status VARCHAR(20) DEFAULT 'Scheduled',
    notes TEXT
);

-- Indexes
CREATE INDEX idx_appointments_patient_id ON appointments(patient_id);
CREATE INDEX idx_appointments_doctor_id ON appointments(doctor_id);
CREATE INDEX idx_appointments_appointment_date ON appointments(appointment_date);
