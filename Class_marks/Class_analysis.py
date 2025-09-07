import pandas as pd
import numpy as np

# Create sample Excel dataset 
data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Amit", "Priya", "Raj", "Sneha", "Kunal",
             "Riya", "Vikas", "Meera", "Arjun", "Anita"],
    "Math": [78, 56, 90, 45, 67, 82, 35, 88, 92, 60],
    "Science": [65, 70, 85, 40, 75, 95, 30, 80, 89, 55],
    "English": [72, 60, 88, 42, 70, 85, 33, 90, 94, 58],
    "Attendance (%)": [90, 85, 95, 70, 88, 92, 65, 93, 97, 80],
    "Sports Score": [8, 6, 9, 4, 7, 10, 3, 8, 9, 5],
    "Cultural Score": [7, 8, 6, 5, 9, 10, 4, 7, 8, 6]
}

df = pd.DataFrame(data)

# Save initial dataset to Excel
df.to_excel("student_data.xlsx", index=False)
print("Sample dataset 'student_data.xlsx' created.\n")

#  Load Data 
df = pd.read_excel("student_data.xlsx")
print("Loaded Data:\n", df.head(), "\n")

#  Step 3: Basic Analysis 
print("Total Students:", len(df))
print("\nAverage Marks:\n", df[["Math", "Science", "English"]].mean())
print("\nHighest Marks:\n", df[["Math", "Science", "English"]].max())
print("\nLowest Marks:\n", df[["Math", "Science", "English"]].min())

#  Step 4: NumPy Calculations 
# Total & Percentage
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Percentage"] = np.round(df["Total"] / 3, 2)

# Standard deviation
print("\nStandard Deviation of Math:", np.std(df["Math"]))

# Ranking
df["Rank"] = df["Percentage"].rank(ascending=False).astype(int)

#  Step 5: Insights 
print("\nTop 5 Students:\n", df.sort_values("Rank").head(5)[["Name", "Percentage", "Rank"]])
print("\nWeak Students (<40%):\n", df[df["Percentage"] < 40][["Name", "Percentage"]])
print("\nCorrelation between Attendance and Percentage:\n", df[["Attendance (%)", "Percentage"]].corr())

#  Step 6: Export Results 
df.to_excel("student_analysis.xlsx", index=False)
print("\nAnalysis saved to 'student_analysis.xlsx'")
