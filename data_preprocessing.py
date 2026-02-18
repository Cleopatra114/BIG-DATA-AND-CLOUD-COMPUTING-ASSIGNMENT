import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Load datasets
sales = pd.read_csv(os.path.join(RAW_DIR, "sales_transactions.csv"))
products = pd.read_csv(os.path.join(RAW_DIR, "products.csv"))
stores = pd.read_csv(os.path.join(RAW_DIR, "stores.csv"))

# Convert date column
sales["date"] = pd.to_datetime(sales["date"])

# Merge datasets
merged_data = sales.merge(products, on="product_id", how="left")
merged_data = merged_data.merge(stores, on="store_id", how="left")

# Save processed data
merged_data.to_csv(
    os.path.join(PROCESSED_DIR, "merged_sales_data.csv"),
    index=False
)

print("Data preprocessing and integration completed.")
