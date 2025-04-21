-- DimPatients
CREATE TABLE DimPatients (
    patient_sk INT IDENTITY(1,1) PRIMARY KEY,
    patient_id INT,
    name VARCHAR(100),
    age INT,
    address VARCHAR(255),
    sickness VARCHAR(255),
    assigned_doctor VARCHAR(100),
    StartDate DATE,
    EndDate DATE,
    IsCurrent BIT
);


-- DimDoctors
CREATE TABLE DimDoctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100)
);

-- DimPrescription
CREATE TABLE DimPrescription (
    prescription_id INT PRIMARY KEY,
    medication VARCHAR(255)
);

-- DimDate
CREATE TABLE DimDate (
    date_id INT PRIMARY KEY,
    FullDate DATE,
    Day INT,
    Month INT,
    Year INT,
    DayOfWeek INT,
    DayName VARCHAR(10),
    MonthName VARCHAR(10),
    Quarter INT,
    IsWeekend BIT
);

-- FactBilling
CREATE TABLE FactBilling (
    billing_id INT PRIMARY KEY,
    patient_sk INT,
    doctor_id INT,
    prescription_id INT,
    date_id INT,
    amount DECIMAL(10, 2),
    payment_status VARCHAR(50),
    payment_method VARCHAR(50),
    FOREIGN KEY (patient_sk) REFERENCES DimPatients(patient_sk),
    FOREIGN KEY (doctor_id) REFERENCES DimDoctors(doctor_id),
    FOREIGN KEY (prescription_id) REFERENCES DimPrescription(prescription_id),
    FOREIGN KEY (date_id) REFERENCES DimDate(date_id)
);

-- Fill DimDate
WITH DateSequence AS (
    SELECT CAST('2020-01-01' AS DATE) AS DateValue
    UNION ALL
    SELECT DATEADD(DAY, 1, DateValue)
    FROM DateSequence
    WHERE DateValue < '2025-12-31'
)
INSERT INTO DimDate (date_id, FullDate, Day, Month, Year, DayOfWeek, DayName, MonthName, Quarter, IsWeekend)
SELECT 
    CONVERT(INT, FORMAT(DateValue, 'yyyyMMdd')) AS date_id,
    DateValue AS FullDate,
    DAY(DateValue) AS Day,
    MONTH(DateValue) AS Month,
    YEAR(DateValue) AS Year,
    DATEPART(WEEKDAY, DateValue) AS DayOfWeek,
    DATENAME(WEEKDAY, DateValue) AS DayName,
    DATENAME(MONTH, DateValue) AS MonthName,
    DATEPART(QUARTER, DateValue) AS Quarter,
    CASE WHEN DATEPART(WEEKDAY, DateValue) IN (1, 7) THEN 1 ELSE 0 END AS IsWeekend
FROM DateSequence
OPTION (MAXRECURSION 32767);
