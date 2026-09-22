# Adult Income Data Preprocessing

## Project Overview

This project focuses on collecting, cleaning, preprocessing, and transforming the UCI Adult Income dataset for data analysis and machine learning applications.

## Dataset

- Source: UCI Adult Income Dataset
- Original records: 32,561
- Final cleaned records: 32,513
- Original features: 15
- Final features: 18

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the Adult Income dataset.
2. Checked the dataset structure and data types.
3. Identified missing values represented by `?`.
4. Replaced missing categorical values using the mode.
5. Removed duplicate records.
6. Detected numerical outliers using the IQR method.
7. Applied suitable outlier capping.
8. Performed feature engineering.
9. Created `age_group`.
10. Created `work_hours_category`.
11. Created `income_encoded`.
12. Verified the final dataset.

## Final Dataset

- Rows: 32,513
- Columns: 18
- Missing values: 0
- Duplicate rows: 0

## Files

- `Data_Preprocessing.ipynb` – Complete preprocessing notebook
- `preprocessing.py` – Python preprocessing script
- `adult_income_clean.csv` – Cleaned dataset
- `requirements.txt` – Required Python libraries
- `adult.zip` – Original dataset files
- PNG files – Preprocessing screenshots and outputs

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook / Google Colab

## Conclusion

The Adult Income dataset was successfully cleaned and preprocessed. Missing values, duplicate records, data quality issues, and relevant outliers were handled, followed by feature engineering. The resulting clean dataset is ready for further analysis and machine learning applications.
