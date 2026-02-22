import pandas as pd

# Load CSV
df = pd.read_csv("simple_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

# ── 1. Preview ────────────────────────────────────────────────
print("=== First 5 rows ===")
print(df.head())

# ── 2. Total Revenue ──────────────────────────────────────────
print("\n=== Total Revenue ===")
print(f"${df['Total_Revenue'].sum():,.2f}")

# ── 3. Revenue by Region ──────────────────────────────────────
print("\n=== Revenue by Region ===")
print(df.groupby("Region")["Total_Revenue"].sum().sort_values(ascending=False))

# ── 4. Revenue by Product ─────────────────────────────────────
print("\n=== Revenue by Product ===")
print(df.groupby("Product")["Total_Revenue"].sum().sort_values(ascending=False))

# ── 5. Units Sold by Product ──────────────────────────────────
print("\n=== Units Sold by Product ===")
print(df.groupby("Product")["Units_Sold"].sum().sort_values(ascending=False))

# ── 6. Sales Rep Performance ──────────────────────────────────
print("\n=== Sales Rep Performance ===")
rep_stats = df.groupby("Sales_Rep").agg(
    Total_Revenue=("Total_Revenue", "sum"),
    Total_Units=("Units_Sold", "sum"),
    Orders=("Order_ID", "count")
).sort_values("Total_Revenue", ascending=False)
print(rep_stats)

# ── 7. Monthly Revenue Trend ──────────────────────────────────
print("\n=== Monthly Revenue Trend ===")
print(df.groupby("Month")["Total_Revenue"].sum())

# ── 8. Average Order Value ────────────────────────────────────
print("\n=== Average Order Value ===")
print(f"${df['Total_Revenue'].mean():,.2f}")

# ── 9. Best-Selling Product per Region ───────────────────────
print("\n=== Best-Selling Product per Region (by Revenue) ===")
best_product = (
    df.groupby(["Region", "Product"])["Total_Revenue"]
    .sum()
    .reset_index()
    .sort_values("Total_Revenue", ascending=False)
    .groupby("Region")
    .first()
)
print(best_product[["Product", "Total_Revenue"]])

# ── 10. Top 5 Orders ──────────────────────────────────────────
print("\n=== Top 5 Orders by Revenue ===")
print(df.nlargest(5, "Total_Revenue")[["Order_ID", "Date", "Product", "Region", "Sales_Rep", "Total_Revenue"]])
