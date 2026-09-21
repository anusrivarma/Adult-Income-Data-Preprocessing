import pandas as pd

# Column names
columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income"
]

# Load the raw dataset
df = pd.read_csv(
    "adult.data",
    names=columns,
    skipinitialspace=True
)

print("Original dataset shape:", df.shape)

# --------------------------------------------------
# 1. Handle missing values
# --------------------------------------------------

# Replace '?' with missing values
df = df.replace("?", pd.NA)

# Fill missing categorical values using mode
categorical_columns = [
    "workclass",
    "occupation",
    "native_country"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 2. Remove duplicate records
# --------------------------------------------------

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print("\nDuplicates before removal:", duplicates_before)
print("Duplicates after removal:", duplicates_after)

# --------------------------------------------------
# 3. Handle selected outliers using IQR
# --------------------------------------------------

outlier_columns = [
    "fnlwgt",
    "hours_per_week"
]

for column in outlier_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[column] = df[column].clip(
        lower=lower_bound,
        upper=upper_bound
    )

print("\nSelected outliers handled successfully.")

# --------------------------------------------------
# 4. Feature Engineering
# --------------------------------------------------

# Age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 50, 65, 100],
    labels=[
        "Young",
        "Young Adult",
        "Adult",
        "Middle Age",
        "Senior"
    ]
)

# Working hours categories
df["work_hours_category"] = pd.cut(
    df["hours_per_week"],
    bins=[0, 35, 40, 60, 100],
    labels=[
        "Part-time",
        "Standard",
        "Overtime",
        "Very High"
    ]
)

# Encode income
df["income_encoded"] = df["income"].map({
    "<=50K": 0,
    ">50K": 1
})

# --------------------------------------------------
# 5. Final validation
# --------------------------------------------------

print("\n========== FINAL DATASET ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# --------------------------------------------------
# 6. Save cleaned dataset
# --------------------------------------------------

df.to_csv(
    "adult_income_clean.csv",
    index=False
)

print("\nClean dataset saved as adult_income_clean.csv")