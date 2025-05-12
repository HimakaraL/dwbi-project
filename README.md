# 🏥 Hospital Management System – Data Warehousing & Business Intelligence Project

## 📌 Project Overview

This project demonstrates the implementation of a **Data Warehousing (DW)** and **Business Intelligence (BI)** solution for a **Hospital Management System**. It integrates multiple data sources, performs ETL processes using **SSIS**, models a star schema data warehouse in **SQL Server**, builds a **multidimensional cube** in **SSAS**, and visualizes insights using **Power BI** and **Excel**.

---

## ⚙️ Tools & Technologies Used

* **Microsoft SQL Server**
* **SSIS (SQL Server Integration Services)**
* **SSAS (SQL Server Analysis Services)**
* **Power BI**
* **Excel**
* **Flat Files (CSV/Excel)**

---

![image](https://github.com/user-attachments/assets/ed53f16e-53e2-480b-8da7-2f3e34fe2e71)


## 📂 Data Sources

1. **MSSQL Tables**

   * `Patients`
   * `Doctors`
   * `Prescriptions`
   * `Appointments`
   * `Billing`

2. **Flat File Sources**

   * CSV or Excel files containing additional data

---

## 🔄 ETL Process with SSIS

Implemented using **SSIS** with:

* **Control Flows**
* **Data Flows**
* **Pre-execute event handlers** to **prevent data duplication**

### SSIS Features Implemented:

* Data extraction from multiple sources
* Data cleansing and transformation
* Loading data into staging and DW layers
* Error handling and logging
* Scheduling and automation

![image](https://github.com/user-attachments/assets/02fc8d89-ef8c-4dcd-8d48-d56d7dc8142c)


---

## 🏗️ Data Warehouse Design

### ✅ **Staging Layer**

Created a staging database to store intermediate data:

* `StgPatients`
* `StgDoctors`
* `StgPrescriptions`
* `StgAppointments`
* `StgBilling`

### ✅ **Star Schema**

Created a DW using star schema modeling:

* **Fact Table**:

  * `FactBilling`
* **Dimension Tables**:

  * `DimPatients`
  * `DimDoctors`
  * `DimPrescriptions`
  * `DimAppointments`

![image](https://github.com/user-attachments/assets/8888a0e7-9427-43ed-a7f6-20b391ecefab)


---

## 📊 SSAS Cube

* Developed a **Multidimensional Cube** using **SSAS**
* Defined **hierarchies** for easy analysis (e.g., date → month → year)
* Processed and deployed the cube for interactive analysis

![image](https://github.com/user-attachments/assets/aadcdabe-579b-49b8-9bb7-1333f579415b)


---

## 📈 Reporting & Visualization

Used the SSAS cube as a data source in:

* **Excel Pivot Tables**
* **Power BI Dashboards**

Generated meaningful reports to analyze:

* Revenue trends
* Doctor performance
* Patient demographics
* Prescription patterns

![image](https://github.com/user-attachments/assets/df32b6c0-e56f-4922-9812-bf1e3215e8db)

![image](https://github.com/user-attachments/assets/74957f31-592f-4349-b569-9d5c89e4b078)

![image](https://github.com/user-attachments/assets/d9f93b99-9ebe-4ee4-9cc2-1355ac98abc3)


---

## ✅ Key Highlights

* Efficient ETL using SSIS with event handling
* Clean star schema design for analytical queries
* Multi-dimensional cube creation with hierarchies
* Dynamic reporting in Power BI and Excel


---

## 🏁 Conclusion

This project showcases a complete DW/BI pipeline from raw hospital data to insightful dashboards. It demonstrates data integration, warehousing, OLAP cube creation, and visualization—all critical for data-driven decision-making in healthcare.

