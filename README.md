# Adult Income Data Preprocessing

## 📌 Project Overview

This project focuses on collecting, cleaning, preprocessing, and transforming a real-world dataset using Python and Pandas.

The **UCI Adult Income Dataset** is used to demonstrate a complete data preprocessing pipeline, including missing-value handling, duplicate removal, data type validation, outlier treatment, and feature engineering.

The project was completed as part of an internship data preprocessing task.

---

## 🎯 Objectives

- Collect a real-world dataset containing more than 1,000 records.
- Inspect and understand the dataset.
- Identify and handle missing values.
- Detect and remove duplicate records.
- Validate data types.
- Detect and handle relevant outliers.
- Perform feature engineering.
- Generate a clean dataset ready for further analysis or machine learning.
- Document the complete preprocessing workflow.

---

## 📊 Dataset

### Dataset Name
**Adult Income Dataset**

### Source
UCI Machine Learning Repository

### Original Dataset Size
- **Rows:** 32,561
- **Columns:** 15

### Dataset Description

The dataset contains demographic and employment-related information such as:

- Age
- Workclass
- Education
- Marital Status
- Occupation
- Relationship
- Race
- Sex
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country
- Income

The target variable is `income`, which represents whether an individual's annual income is above or below $50K.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Google Colab
- GitHub

---

## 🔄 Preprocessing Pipeline

### 1. Data Collection

The UCI Adult Income Dataset was collected from the UCI Machine Learning Repository.

The dataset contains more than the required 1,000 samples.

### 2. Data Loading

The dataset was loaded into a Pandas DataFrame and column names were assigned based on the dataset documentation.

### 3. Missing Value Handling

The dataset represented missing categorical values using `?`.

These values were converted into proper missing values and handled using the mode of the respective categorical column.

Missing values were found in:

- `workclass`
- `occupation`
- `native_country`

### 4. Duplicate Removal

Duplicate records were identified and removed.

- Duplicate records detected: **24**
- Duplicate records after cleaning: **0**

### 5. Data Type Validation

The data types of all columns were inspected.

Numerical variables were stored using integer data types, while categorical variables were stored as object/string types.

### 6. Outlier Detection

The Interquartile Range (IQR) method was used to identify potential outliers in numerical features.

Selected numerical features were treated using IQR-based capping while preserving the original observations.

### 7. Feature Engineering

Three new features were created:

#### `age_group`

Age was divided into meaningful groups:

- Young
- Young Adult
- Adult
- Middle Age
- Senior

#### `work_hours_category`

Weekly working hours were categorized into:

- Part-time
- Standard
- Overtime
- Very High

#### `income_encoded`

Income was converted into numerical format:

- `<=50K` → `0`
- `>50K` → `1`

---

## 📈 Final Dataset

After preprocessing:

- **Rows:** 32,537
- **Columns:** 18
- **Missing values:** 0
- **Duplicate rows:** 0

The final dataset contains the original features along with the engineered features.

---

## 📁 Project Structure

```text
Adult-Income-Data-Preprocessing/
│
├── Data_Preprocessing.ipynb
├── README.md
├── adult.zip
└── adult_income_clean.csv
