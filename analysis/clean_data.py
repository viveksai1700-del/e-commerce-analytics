import pandas as pd
import os

# Paths
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data")
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "cleaned_data")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def load_csv(filename):
    path = os.path.join(DATA_FOLDER, filename)
    return pd.read_csv(path)


# --------------------------------------------------
# 1. ORDERS
# --------------------------------------------------

orders = load_csv("olist_orders_dataset.csv")

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# Delivery time in days
orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.total_seconds() / (60 * 60 * 24)

# Estimated delivery delay
orders["delivery_delay_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_estimated_delivery_date"]
).dt.total_seconds() / (60 * 60 * 24)

orders.to_csv(
    os.path.join(OUTPUT_FOLDER, "orders_clean.csv"),
    index=False
)


# --------------------------------------------------
# 2. ORDER ITEMS
# --------------------------------------------------

order_items = load_csv("olist_order_items_dataset.csv")

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

# Total item value including freight
order_items["total_item_value"] = (
    order_items["price"] + order_items["freight_value"]
)

order_items.to_csv(
    os.path.join(OUTPUT_FOLDER, "order_items_clean.csv"),
    index=False
)


# --------------------------------------------------
# 3. PAYMENTS
# --------------------------------------------------

payments = load_csv("olist_order_payments_dataset.csv")

payments.to_csv(
    os.path.join(OUTPUT_FOLDER, "payments_clean.csv"),
    index=False
)


# --------------------------------------------------
# 4. CUSTOMERS
# --------------------------------------------------

customers = load_csv("olist_customers_dataset.csv")

customers.to_csv(
    os.path.join(OUTPUT_FOLDER, "customers_clean.csv"),
    index=False
)


# --------------------------------------------------
# 5. PRODUCTS
# --------------------------------------------------

products = load_csv("olist_products_dataset.csv")

# Missing categories
products["product_category_name"] = products[
    "product_category_name"
].fillna("unknown")

# Missing numerical product information
numeric_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for col in numeric_columns:
    products[col] = products[col].fillna(0)

products.to_csv(
    os.path.join(OUTPUT_FOLDER, "products_clean.csv"),
    index=False
)


# --------------------------------------------------
# 6. SELLERS
# --------------------------------------------------

sellers = load_csv("olist_sellers_dataset.csv")

sellers.to_csv(
    os.path.join(OUTPUT_FOLDER, "sellers_clean.csv"),
    index=False
)


# --------------------------------------------------
# 7. REVIEWS
# --------------------------------------------------

reviews = load_csv("olist_order_reviews_dataset.csv")

reviews["review_comment_title"] = reviews[
    "review_comment_title"
].fillna("No comment")

reviews["review_comment_message"] = reviews[
    "review_comment_message"
].fillna("No comment")

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

reviews.to_csv(
    os.path.join(OUTPUT_FOLDER, "reviews_clean.csv"),
    index=False
)


# --------------------------------------------------
# 8. GEOLOCATION
# --------------------------------------------------

geolocation = load_csv("olist_geolocation_dataset.csv")

# Keep one coordinate record per ZIP prefix
geolocation_clean = (
    geolocation
    .groupby("geolocation_zip_code_prefix", as_index=False)
    .agg({
        "geolocation_lat": "mean",
        "geolocation_lng": "mean",
        "geolocation_city": "first",
        "geolocation_state": "first"
    })
)

geolocation_clean.to_csv(
    os.path.join(OUTPUT_FOLDER, "geolocation_clean.csv"),
    index=False
)


# --------------------------------------------------
# 9. CATEGORY TRANSLATION
# --------------------------------------------------

translation = load_csv(
    "product_category_name_translation.csv"
)

translation.to_csv(
    os.path.join(OUTPUT_FOLDER, "category_translation_clean.csv"),
    index=False
)


print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(f"\nCleaned files saved to:")
print(OUTPUT_FOLDER)

print("\nFiles created:")

for file in os.listdir(OUTPUT_FOLDER):
    print(" -", file)