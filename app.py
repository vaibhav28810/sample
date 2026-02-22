import pandas as pd

# Load CSV
df = pd.read_csv("simple_sales_data.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Total revenue
print("\nTotal Revenue:", df["Total_Revenue"].sum())

# Revenue by region
print("\nRevenue by Region:")
print(df.groupby("Region")["Total_Revenue"].sum())