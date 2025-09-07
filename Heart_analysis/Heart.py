import pandas as pd
import numpy as np

# 1. Load Dataset
df = pd.read_csv("heart.csv")
print("Data Loaded Successfully!")
print(df.head())

# 2. Data Cleaning
# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print("\nMissing values per column:\n", df.isnull().sum())

# 3. Basic Analysis
print("\n--- Basic Stats ---")
print(df.describe())

# Gender distribution
gender_count = df['sex'].value_counts()

# Heart disease by gender
disease_by_gender = df.groupby('sex')['target'].mean()

# Age group analysis
df['age_group'] = pd.cut(df['age'], bins=[20,30,40,50,60,70,80],
labels=["20s","30s","40s","50s","60s","70s"])
disease_by_age = df.groupby('age_group')['target'].mean()

# 4. NumPy Analysis
chol = df['chol'].to_numpy()
thalach = df['thalach'].to_numpy()

chol_mean = np.mean(chol)
chol_std = np.std(chol)
corr_age_thalach = np.corrcoef(df['age'], thalach)[0,1]

print("\n--- NumPy Analysis ---")
print("Mean Cholesterol:", chol_mean)
print("Std Dev Cholesterol:", chol_std)
print("Correlation (Age vs Max Heart Rate):", corr_age_thalach)

# Custom Risk Score
df['risk_score'] = 0.3*df['age'] + 0.2*df['chol'] + 0.5*(220 - df['thalach'])

# 5. Advanced Analysis
avg_risk_gender = df.groupby('sex')['risk_score'].mean()
risk_comparison = df.groupby('target')['risk_score'].mean()
high_chol_patients = df[df['chol'] > 300]

# 6. Export Reports
# Save full dataset with new columns
df.to_excel("heart_disease_analysis.xlsx", index=False)

# Create summary report
summary = {
    "Gender distribution": gender_count.to_dict(),
    "Disease by gender": disease_by_gender.to_dict(),
    "Disease by age group": disease_by_age.to_dict(),
    "Avg risk by gender": avg_risk_gender.to_dict(),
    "Risk comparison (Disease=1 vs No Disease=0)": risk_comparison.to_dict(),
    "High cholesterol patients count (>300)": len(high_chol_patients)
}

summary_df = pd.DataFrame.from_dict(summary, orient='index').transpose()
summary_df.to_excel("heart_disease_summary.xlsx", index=False)

print("\nReports generated successfully!")
print("-> heart_disease_analysis.xlsx")
print("-> heart_disease_summary.xlsx")
