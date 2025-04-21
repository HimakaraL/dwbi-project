CREATE TABLE doctors (
	doctorId INT PRIMARY KEY,
	registrationNo INT,
	name VARCHAR(100),
	experience INT,
	specialization VARCHAR(100),
	phoneNo VARCHAR(50),
	address VARCHAR(255)
);

CREATE TABLE patients (
	patientId INT PRIMARY KEY,
	name VARCHAR(100),
	age INT,
	phoneNo VARCHAR(50),
	address VARCHAR(255),
	sickness VARCHAR(50),
	assigned_doctor VARCHAR(100)
);

CREATE TABLE prescriptions (
	prescriptionId INT PRIMARY KEY,
	appointmentId INT,
	medication VARCHAR(255),
	dosage VARCHAR(255),
	frequency VARCHAR(255),
	duration VARCHAR(255)
);

CREATE TABLE appointments (
	appointmentId INT PRIMARY KEY,
	patientId INT,
	doctorId INT,
	date VARCHAR(255),
	time VARCHAR(20), 
	status VARCHAR(255)
);

CREATE TABLE billing (
	billingId INT PRIMARY KEY,
	appointmentId INT,
	amount INT,
	paymentStatus VARCHAR(50),
	paymentMethod VARCHAR(50)
);
