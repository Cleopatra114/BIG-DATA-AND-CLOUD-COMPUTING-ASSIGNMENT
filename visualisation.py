import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "merged_sales_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "tables")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

# Monthly sales
monthly_sales = (
    df.groupby("month")["total_price"]
    .sum()
    .reset_index(name="monthly_revenue")
)

# Top products
top_products = (
    df.groupby("product_name")["total_price"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index(name="total_revenue")
)

# Save summary statistics
summary = monthly_sales.merge(
    top_products,
    how="cross"
)

summary.to_csv(
    os.path.join(OUTPUT_DIR, "summary_statistics.csv"),
    index=False
)

print("Sales analysis completed.")
