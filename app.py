from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta
import os

os.makedirs("CSVs", exist_ok=True)
faker = Faker()

# 1. Mapping Sickness to Specialization
sickness_to_specialization = {
    'Fever': 'General Physician',
    'Cold': 'General Physician',
    'Headache': 'General Physician',
    'Stomachache': 'Gastroenterologist',
    'Cough': 'General Physician',
    'Flu': 'General Physician',
    'Allergy': 'General Physician',
    'Infection': 'General Physician',
    'Back Pain': 'Orthopedist',
    'Joint Pain': 'Orthopedist',
    'Diarrhea': 'Gastroenterologist',
    'Nausea': 'Gastroenterologist',
    'Vomiting': 'Gastroenterologist',
    'Fatigue': 'General Physician',
    'Dizziness': 'General Physician',
    'Chest Pain': 'Cardiologist',
    'Shortness of breath': 'Pulmonologist',
    'Rash': 'Dermatologist',
    'Skin Infection': 'Dermatologist',
    'Muscle Pain': 'Orthopedist',
    'Sore Throat': 'General Physician',
    'Pneumonia': 'Pulmonologist',
    'Bronchitis': 'Pulmonologist',
    'Asthma': 'Pulmonologist',
    'Diabetes': 'Endocrinologist',
    'Hypertension': 'Cardiologist',
    'Heart Disease': 'Cardiologist',
    'Kidney Disease': 'Nephrologist',
    'Liver Disease': 'Gastroenterologist',
    'Thyroid Disorder': 'Endocrinologist',
    'Gastroenteritis': 'Gastroenterologist',
    'Urinary Tract Infection': 'Nephrologist',
    'Constipation': 'Gastroenterologist',
    'Hemorrhoids': 'Gastroenterologist',
    'Anxiety': 'Psychiatrist'
}

# Sickness weights for realism
sickness_weights = {
    'Fever': 0.12, 'Cold': 0.12, 'Headache': 0.1, 'Stomachache': 0.06,
    'Cough': 0.1, 'Flu': 0.08, 'Allergy': 0.04, 'Infection': 0.04,
    'Back Pain': 0.05, 'Joint Pain': 0.04, 'Diarrhea': 0.03, 'Nausea': 0.02,
    'Vomiting': 0.02, 'Fatigue': 0.04, 'Dizziness': 0.03, 'Chest Pain': 0.02,
    'Shortness of breath': 0.02, 'Rash': 0.02, 'Skin Infection': 0.01,
    'Muscle Pain': 0.01, 'Sore Throat': 0.03, 'Pneumonia': 0.01,
    'Bronchitis': 0.01, 'Asthma': 0.01, 'Diabetes': 0.02, 'Hypertension': 0.02,
    'Heart Disease': 0.01, 'Kidney Disease': 0.01, 'Liver Disease': 0.01,
    'Thyroid Disorder': 0.01, 'Gastroenteritis': 0.01,
    'Urinary Tract Infection': 0.01, 'Constipation': 0.01,
    'Hemorrhoids': 0.01, 'Anxiety': 0.01
}

# 2. Medications List
medications = ['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Metformin', 'Amlodipine',
    'Simvastatin', 'Omeprazole', 'Levothyroxine', 'Lisinopril', 'Sertraline',
    'Atorvastatin', 'Gabapentin', 'Albuterol', 'Fluticasone', 'Montelukast',
    'Ciprofloxacin', 'Azithromycin', 'Hydrochlorothiazide', 'Furosemide',
    'Warfarin', 'Clopidogrel', 'Insulin', 'Prednisone', 'Cetirizine',
    'Diphenhydramine', 'Loratadine', 'Ranitidine', 'Esomeprazole',
    'Pantoprazole', 'Duloxetine', 'Venlafaxine', 'Bupropion', 'Citalopram',
    'Escitalopram', 'Fluoxetine', 'Paroxetine', 'Trazodone',
    'Buspirone', 'Lorazepam', 'Diazepam', 'Alprazolam', 'Clonazepam',
    'Zolpidem', 'Eszopiclone', 'Ramelteon', 'Melatonin', 'Sildenafil',
    'Tadalafil', 'Finasteride', 'Dutasteride', 'Levitra', 'Cialis',
    'Viagra', 'Nitroglycerin', 'Aspirin', 'Clonidine', 'Carvedilol',
    'Metoprolol', 'Propranolol', 'Atenolol', 'Bisoprolol', 'Nebivolol',
    'Diltiazem', 'Verapamil', 'Nifedipine', 'Felodipine']

# 3. Doctor Generation
def generate_doctor_data(n):
    doctors = []
    for i in range(n):
        specialization = random.choice(list(set(sickness_to_specialization.values())))
        doctors.append({
            'doctorId': i,
            'registrationNo': faker.unique.random_int(min=1000, max=9999),
            'name': faker.name(),
            'experience': random.randint(1, 30),
            'specialization': specialization,
            'phoneNo': faker.phone_number(),
            'address': faker.address()
        })
    return doctors

doctors_data = generate_doctor_data(100)

# 4. Patient Generation with Doctor Assignment
def generate_patient_data(n):
    patients = []
    specialization_map = {}
    for doc in doctors_data:
        specialization_map.setdefault(doc['specialization'], []).append(doc['doctorId'])

    for i in range(n):
        sickness = random.choices(list(sickness_weights.keys()), weights=sickness_weights.values())[0]
        specialization = sickness_to_specialization[sickness]
        assigned_doctor = random.choice(specialization_map.get(specialization, [None]))
        patients.append({
            'patientId': i,
            'name': faker.name(),
            'age': random.randint(1, 90),
            'phoneNo': faker.phone_number(),
            'address': faker.address(),
            'sickness': sickness,
            'assigned_doctor': assigned_doctor
        })
    return patients

patients_data = generate_patient_data(1000)

# 5. Appointment Generation (at least 1 year of data)
def generate_appointment_data(n):
    appointments = []
    for i in range(n):
        patient = random.choice(patients_data)
        if not patient['assigned_doctor']:
            continue
        date = faker.date_between(start_date='-1y', end_date='today')
        appointments.append({
            'appointmentId': i,
            'patientId': patient['patientId'],
            'doctorId': patient['assigned_doctor'],
            'date': date.strftime('%Y-%m-%d'),
            'time': faker.time(),
            'status': random.choices(['Scheduled', 'Completed', 'Cancelled'], weights=[0.2, 0.7, 0.1])[0]
        })
    return appointments

appointments_data = generate_appointment_data(2000)

# 6. Prescription Generation (only for Completed appointments)
def generate_prescription_data(appointments_data):
    prescriptions = []
    completed = [a for a in appointments_data if a['status'] == 'Completed']
    for i, app in enumerate(random.sample(completed, min(1500, len(completed)))):
        num_meds = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
        prescriptions.append({
            'prescriptionId': i,
            'appointmentId': app['appointmentId'],
            'medication': ', '.join(random.sample(medications, num_meds)),
            'dosage': random.choice(['Once a day', 'Twice a day', 'Three times a day']),
            'frequency': random.choice(['Morning', 'Afternoon', 'Evening']),
            'duration': random.choice(['1 week', '2 weeks', '1 month'])
        })
    return prescriptions

prescriptions_data = generate_prescription_data(appointments_data)

# 7. Billing Generation
def generate_billing_data(appointments_data):
    billings = []
    for i, app in enumerate(appointments_data):
        billings.append({
            'billingId': i,
            'appointmentId': app['appointmentId'],
            'amount': random.randint(500, 5000),
            'paymentStatus': random.choice(['Paid', 'Pending', 'Failed']),
            'paymentMethod': random.choice(['Cash', 'Credit Card', 'Debit Card', 'Insurance'])
        })
    return billings

billing_data = generate_billing_data(appointments_data)

# 8. Export to CSV
pd.DataFrame(doctors_data).to_csv("CSVs/doctors.csv", index=False)
pd.DataFrame(patients_data).to_csv("CSVs/patients.csv", index=False)
pd.DataFrame(appointments_data).to_csv("CSVs/appointments.csv", index=False)
pd.DataFrame(prescriptions_data).to_csv("CSVs/prescriptions.csv", index=False)
pd.DataFrame(billing_data).to_csv("CSVs/billing.csv", index=False)

print("✅ All datasets generated and exported successfully!")
