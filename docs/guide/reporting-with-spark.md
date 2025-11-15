# Reporting with Spark

> Analyze and visualize stored data to generate business intelligence insights
> Common BI workflow: Connect / Load / Query / Explore / Visualize

## Task 1: Set Up Spark

Use Spark with a **JDBC connection** to read data from a database.

See the instructions at [Install Spark](../installs/install-spark.md) and follow the steps to install a **JDBC driver** and make a lib/ folder in your root project repository folder to hold the jar file.

You may need to use the **full absolute path** in the Spark configuration, and restart the Spark session in Jupyter.

## Task 2: Load DW Tables into Spark

Establish a connection between Spark and a data warehouse (e.g., `smart_sales.db`).


```python

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SmartSalesDW")
    .config("spark.driver.extraClassPath", "/absolute/path/to/lib/sqlite-jdbc.jar")
    .getOrCreate()
)

# Load tables using JDBC
df_sales = spark.read.format("jdbc").options(
    url="jdbc:sqlite:/absolute/path/to/smart_sales.db",
    dbtable="sales",
    driver="org.sqlite.JDBC"
).load()

df_customer = spark.read.format("jdbc").options(
    url="jdbc:sqlite:/absolute/path/to/smart_sales.db",
    dbtable="customer",
    driver="org.sqlite.JDBC"
).load()

```

## Task 3: Query & Aggregate Data

Use **Spark SQL** to write a custom SQL queries.

We'll use Spark SQL to perform a grouped query, then convert the result to a Pandas DataFrame for visualization.

Write a Spark SQL query for total revenue per customer.
Store the results in a Pandas DataFrame for visualization.
Review the results.

Register Spark DataFrames as temporary views (if not already done):

```python
df_sales.createOrReplaceTempView("sales")
df_customer.createOrReplaceTempView("customer")
# TODO: add products as well
```


Write a Spark SQL query:

```python
df_top_customers = spark.sql("""
SELECT c.name, SUM(s.amount) AS total_spent
FROM sales s
JOIN customer c ON s.customer_id = c.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
""")
```

Show Spark SQL results:

```python
df_top_customers.show()
```

Convert to Pandas Dataframes for use with charts:

```
import pandas as pd  # place at top of notebook

df_top_customers_pd = df_top_customers.toPandas()
```

## Task 4: Slice, Dice, and Drilldown

Implement slicing, dicing, and drilldown operations using Spark DataFrame transformations and aggregations.

- **Slicing:** Filter data by date range
- **Dicing:** Group data by two categorical dimensions
- **Drilldown**: Aggregate sales by Year > Quarter > Month

```python
# Slicing
df_filtered = df_sales.filter(df_sales.order_date >= "2023-01-01")

# Dicing (product × region)
df_sales.groupby("product_category", "region").sum("amount").show()

# Drilldown (year > quarter > month)
df_sales.groupby("year", "quarter", "month").sum("amount").show()
```

## Task 5: Create Visuals

Create visuals to interpret results.

Common charts:

- Create a bar chart for **Top Customers** (or similar)
- Create a line chart for **Sales Trends** (or similar trend)
- Add a slicer for product categories (or other categorical field) using filtered DataFrames

Create visuals using **Seaborn** and **matplotlib**.

All imports at the top, organized:

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

Example chart:

```python
sns.barplot(data=df_top_customers_pd, x="name", y="total_spent")
plt.xticks(rotation=45)
plt.show()
```
