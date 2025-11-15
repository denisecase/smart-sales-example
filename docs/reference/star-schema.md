# Star Schema Overview for `smart-sales-example`

This project uses a clean, minimal **star schema** to illustrate the core concepts of business intelligence (BI) data modeling.
It provides a simple example as part of a BI project incorporating ETL, SQL, OLAP, and analytics workflows in a modern Python and SQLite (or DuckDB) pipeline.

---

## Initial Star Schema

We have **one fact table** and **two dimension tables**:

### **Dimension: `customer`**
```sql
customer_id  INTEGER PRIMARY KEY
name         TEXT
region       TEXT
join_date    TEXT
```

### **Dimension: `product`**
```sql
product_id    INTEGER PRIMARY KEY
product_name  TEXT
category      TEXT
unit_price    REAL
```

### **Fact: `sale`**
```sql
sale_id      INTEGER PRIMARY KEY
customer_id  INTEGER  -- FK to customer
product_id   INTEGER  -- FK to product
sale_amount  REAL     -- measure
sale_date    TEXT     -- transaction date
```

The **grain** of the fact table is:
**one row per sale event** (customer × product × date).

---

## Star Schema

A data model is a star schema when it contains:

- A **central fact table** containing numeric/measurable events: `sale.sale_amount`
- One or more **dimension tables** containing descriptive attributes: `customer`, `product`
- **Foreign key relationships** from fact to dimensions: `sale.customer_id`, `sale.product_id`
- A well-defined **grain**: each fact row is a single sale event

A star schema makes it easy to write analytic queries such as:

- Sales by customer
- Sales by product or category
- Sales by region
- Sales by month or year
- Top 10 customers by revenue
- Product category profitability
- etc.

Our project is small but demonstrates a **full BI lifecycle**:

- Data cleaning
- Conformed dimensions
- Fact table construction
- ETL
- OLAP queries (`GROUP BY`, aggregates, drill-downs)
- Visualizations

---

## Modifications

- **Add your new columns** to the dimension CSVs
- **Extend the schema** with your additional attributes
- **Transform any messy headers** and use clean snake_case throughout
- **Load the warehouse** with the ETL pipeline
- Once in there, we will build:
  - Aggregation queries
  - Multi-dimensional reports
  - Simple dashboards
- Perform OLAP-style analysis:
  - Drill down by category
  - Slice by region
  - Trend analysis using `sale_date`

This repo illustrates **a complete, end-to-end BI project**.

---

## Additional Improvements

To align with more formal BI/warehouse naming conventions:

### 1. Table naming
Rename:

| Current       | Improved                |
|---------------|--------------------------|
| `customer`    | `dim_customer`           |
| `product`     | `dim_product`            |
| `sale`        | `fact_sale` or `fact_sales` |

This is common in Snowflake, Redshift, dbt, and enterprise BI.

### 2. Add a proper date dimension
Instead of storing `sale_date` in the fact table:

- create a `dim_date`
- join it via `date_id`
- allow easy year/month/week rollups

### 3. Add more measures
Examples:

- `quantity`
- `discount_amount`
- `profit` (calculated)
- `unit_cost`

### 4. Add more descriptive attributes
Extend:

- **Customer**: age, loyalty segment, state, customer_type
- **Product**: brand, supplier, subcategory

New attributes expand analytic possibilities.

