from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum
from .engine import main_engine

# Base class for all models
Base = declarative_base()

# Enum for connection state
class ConnectionState(PyEnum):
    CONNECTED = 0
    DISCONNECTED = 1

# Define the Doctor model
class Doctor(Base):
    __tablename__ = 'doctors'
    
    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    specialty = Column(String(100), nullable=False)
    contact_number = Column(String(20))
    email = Column(String(100))
    office_number = Column(String(20))
    
    appointments = relationship("Appointment", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor(doctor_id={self.doctor_id}, first_name={self.first_name}, last_name={self.last_name})>"

# Define the Patient model
class Patient(Base):
    __tablename__ = 'patients'
    
    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10))
    contact_number = Column(String(20))
    email = Column(String(100))
    address = Column(String(200))

    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        return f"<Patient(patient_id={self.patient_id}, first_name={self.first_name}, last_name={self.last_name})>"

# Define the Appointment model
class Appointment(Base):
    __tablename__ = 'appointments'
    
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    status = Column(Enum(ConnectionState), nullable=False)
    notes = Column(String(200))
    
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(appointment_id={self.appointment_id}, patient_id={self.patient_id}, doctor_id={self.doctor_id})>"

def init_db() -> bool:
    if hasattr(init_db, "init_success"):
        return True
    try:
        Base.metadata.create_all(main_engine)
        init_db.init_success = True
        return True
    except Exception as e:
        print(f"Error occurred while creating tables: {e}")
        return False

