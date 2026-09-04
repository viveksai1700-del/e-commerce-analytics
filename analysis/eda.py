import pandas as pd
import os

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data")

files = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv"
]

for file in files:
    path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(path)

    print("\n" + "=" * 60)
    print(f"DATASET: {file}")
    print("=" * 60)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print(f"\nDuplicate Rows: {df.duplicated().sum()}")