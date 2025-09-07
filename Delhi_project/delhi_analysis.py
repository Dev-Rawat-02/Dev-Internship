import pandas as pd
import numpy as np


# Step 1: Create / Simulate Data

np.random.seed(42)

data = {
    "Date": pd.date_range("2024-01-01", periods=100, freq="D"),
    "Time": np.random.choice(["08:00", "12:00", "18:00", "22:00"], 100),
    "Location": np.random.choice(
        ["Connaught Place", "Saket", "NH-24", "Dwarka", "Noida Border"], 100
    ),
    "Vehicle_Count": np.random.randint(100, 2000, 100),
    "Accidents": np.random.randint(0, 5, 100),
    "Avg_Speed": np.random.randint(20, 80, 100),
    "AQI": np.random.randint(100, 400, 100),
}

df = pd.DataFrame(data)
print("Sample Data:\n", df.head())


# Step 2: Clean Data

df.drop_duplicates(inplace=True)
print("\nMissing Values:\n", df.isnull().sum())


# Step 3: Analysis

print("\nAverage Traffic by Location:\n", df.groupby("Location")["Vehicle_Count"].mean())
print("\nAverage Traffic by Time:\n", df.groupby("Time")["Vehicle_Count"].mean())
print("\nCorrelation (Traffic vs AQI):\n", df[["Vehicle_Count", "AQI"]].corr())
print("\nAccident Hotspots:\n", df.groupby("Location")["Accidents"].sum())
print("\nTop 5 Congested Days:\n", df.nlargest(5, "Vehicle_Count")[["Date", "Location", "Vehicle_Count"]])


# Step 4: Export Results

df.to_csv("delhi_traffic_report.csv", index=False)
print("\nReport saved as delhi_traffic_report.csv")
