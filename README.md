# E-Commerce Sales & Customer Analytics

An end-to-end data analytics project analyzing e-commerce sales, customer behavior, product performance, and delivery operations using Python, PostgreSQL, SQL, and Power BI.

## Project Overview

This project uses the Brazilian E-Commerce Public Dataset by Olist to analyze approximately 100,000 e-commerce orders and uncover actionable business insights.

The project follows a complete analytics workflow:

**Data Cleaning → Exploratory Data Analysis → PostgreSQL → SQL Analytics → Power BI Dashboard**

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Power BI
- Git & GitHub

## Dataset

The project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about:

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Reviews
- Geolocation
- Product Categories

Raw CSV files are intentionally excluded from this repository using `.gitignore`.

## Data Preparation

Python was used to:

- Inspect dataset structure and data quality
- Identify missing values and duplicates
- Convert date columns to appropriate formats
- Calculate delivery duration
- Calculate delivery delay
- Calculate total item value
- Handle missing product and review information
- Deduplicate and aggregate geolocation data
- Export cleaned datasets for PostgreSQL analysis

## SQL Analysis

PostgreSQL was used to perform business-focused analysis including:

- Overall revenue and order performance.
- Monthly revenue trends.
- Revenue by product category.
- Top products by revenue.
- Repeat customer analysis
- Revenue by customer state
- Delivery performance
- Delivery delay analysis
- Delivery performance vs review scores
- Payment method analysis
- Top customers by spending
- Customer value segmentation
- Category revenue ranking using window functions
- Month-over-month revenue growth
- Customer lifetime value
- Customer acquisition trends
- RFM-style customer segmentation

## Power BI Dashboard

The Power BI dashboard provides an interactive overview of the business.

### Key KPIs

- Total Revenue.
- Total Orders.
- Unique Customers.
- Average Order Value.
- Repeat Customer Rate.

### Dashboard Visualizations

- Monthly Revenue Trend.
- Top 10 Categories by Revenue.
- Top 10 Products by Revenue.

## Key Business Insights

The analysis helps answer questions such as:

- Which product categories generate the most revenue?
- Which products contribute the most to sales?
- How is revenue changing over time?
- What percentage of customers make repeat purchases?
- Which customer segments contribute the most revenue?
- Which regions generate the highest sales?
- How does delivery performance affect customer satisfaction?
- Which payment methods are most commonly used?

## Project Structure

```text
E commerce analytics/
│
├── data/
│   └── Raw CSV files
│
├── analysis/
│   ├── eda.py
│   ├── clean_data.py
│   └── cleaned_data/
│
├── sql/
│   └── SQL analysis queries
│
├── powerbi/
│   └── Power BI dashboard
│
└── README.md