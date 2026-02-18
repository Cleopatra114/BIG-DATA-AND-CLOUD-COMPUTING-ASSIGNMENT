import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Define directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

# ---------------------------
# Products Data
# ---------------------------
products = pd.DataFrame({
    "product_id": range(1, 21),
    "product_name": [f"Product_{i}" for i in range(1, 21)],
    "category": np.random.choice(
        ["Electronics", "Clothing", "Groceries"], 20
    ),
    "unit_price": np.random.randint(5, 200, 20)
})

# ---------------------------
# Stores Data
# ---------------------------
stores = pd.DataFrame({
    "store_id": range(1, 6),
    "city": ["London", "Manchester", "Birmingham", "Leeds", "Liverpool"],
    "region": ["South", "North", "Midlands", "North", "North"]
})

# ---------------------------
# Customers Data
# ---------------------------
customers = pd.DataFrame({
    "customer_id": range(1, 101),
    "age": np.random.randint(18, 70, 100),
    "gender": np.random.choice(["Male", "Female"], 100),
    "loyalty_member": np.random.choice(["Yes", "No"], 100)
})

# ---------------------------
# Sales Transactions Data
# ---------------------------
dates = pd.date_range(start="2024-01-01", end="2024-12-31")

sales = pd.DataFrame({
    "transaction_id": range(1, 1001),
    "date": np.random.choice(dates, 1000),
    "store_id": np.random.choice(stores["store_id"], 1000),
    "product_id": np.random.choice(products["product_id"], 1000),
    "quantity": np.random.randint(1, 6, 1000)
})

sales = sales.merge(
    products[["product_id", "unit_price"]],
    on="product_id",
    how="left"
)

sales["total_price"] = sales["quantity"] * sales["unit_price"]

# ---------------------------
# Save CSV Files
# ---------------------------
products.to_csv(os.path.join(RAW_DIR, "products.csv"), index=False)
stores.to_csv(os.path.join(RAW_DIR, "stores.csv"), index=False)
customers.to_csv(os.path.join(RAW_DIR, "customers.csv"), index=False)
sales.to_csv(os.path.join(RAW_DIR, "sales_transactions.csv"), index=False)

print("Synthetic retail datasets generated successfully.")
