# (Optional): Finalizing Your Data Warehouse

This page includes optional enhancements.
These steps prepare your warehouse for richer analytics and time-based reporting.

## (Optional) Task 1. Standardize Table Naming

Many BI environments use these conventions:

- **dim\_\*** tables hold descriptive attributes
- **fact\_\*** tables hold measurable events

If you choose to follow this convention, rename your tables accordingly:

```
customer     becomes `dim_customer`
product      becomes `dim_product`
sale         becomes `fact_sale`
```

## (Optional) Task 2. Add a Date Dimension

A `dim_date` table supports:

- time slicing
- drilldown
- grouping by year, quarter, month
- consistent reporting across tools

### Example schema:

```sql
CREATE TABLE IF NOT EXISTS dim_date (
    date_key TEXT PRIMARY KEY,    -- 'YYYY-MM-DD'
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name TEXT,
    day INTEGER,
    weekday_name TEXT
);
```

Generate this table from the dates in your fact table.

## (Optional) Task 3. Ensure Foreign Keys Align

Make sure your fact table points to dimensions using matching keys.

Examples:

```
`fact_sale.customer_id` points to `dim_customer.customer_id`
`fact_sale.product_id`  points to `dim_product.product_id`
`fact_sale.date_key`    points to `dim_date.date_key`
```

This alignment supports slicing, dicing, and drilldown.
