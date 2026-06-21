Bike Store Data Engineering Pipeline


 Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using Python and PostgreSQL.
The Bike Store dataset contains customer, order, product, store, staff, and inventory data spread across multiple relational tables. While the dataset is small, the project is designed to simulate how real organizations ingest, validate, transform, and organize business data for analytics and reporting.



Business Problem

Business data is often stored across multiple operational systems and tables.
Answering questions such as:

* Which products generate the highest revenue?
* Which stores perform best?
* How much inventory is available at each location?
* What are the sales trends over time?

becomes difficult when data is scattered across raw files and normalized tables.



 Solution

Built a complete ETL pipeline that:

* Extracts raw CSV data
* Loads data into a PostgreSQL staging layer
* Performs data validation checks
* Transforms data into a Star Schema warehouse model
* Loads fact and dimension tables
* Automates the entire workflow through a single pipeline


 
 Architecture

Raw CSV Files

↓ Extract

Staging Layer

↓ Validation

Data Warehouse

↓ Star Schema

Fact & Dimension Tables

↓ Analytics

Power BI / Reporting ( future)







Technologies Used

* Python
* PostgreSQL
* Pandas
* SQLAlchemy
* Git & GitHub




Data Warehouse Model

Dimension Tables

* dim_customer
* dim_product
* dim_store
* dim_staff
* dim_date

Fact Tables

fact_sales
fact_inventory



 Key Features

* End-to-End ETL Pipeline
* Data Validation Layer
* Star Schema Modeling
* Automated Pipeline Execution
* Logging & Monitoring
* Re-runnable (Idempotent) Pipeline
* Git Version Control



 Pipeline Execution

```bash
python3 pipeline.py
```

The pipeline automatically:

1. Creates schemas and tables
2. Loads staging data
3. Validates data quality
4. Loads dimensions
5. Loads fact tables
6. Generates execution logs

---

 Why Data Engineering?

While analytics can be performed directly on CSV files for small datasets, organizations work with millions of records generated daily from multiple systems.

Data Engineering helps by:

* Centralizing data
* Improving query performance
* Automating data workflows
* Enabling scalable reporting and analytics
* Supporting business decision-making
  



Future Improvements

* Power BI Dashboard
* AWS S3 Integration
* Incremental Data Loading
* CI/CD Automation



Author

Nitish Kumar Kushwaha

BCA (Data Science)

