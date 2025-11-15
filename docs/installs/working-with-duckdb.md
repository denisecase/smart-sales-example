# Working with DuckDB

> Using DuckDB with Python, Power BI, and Spark SQL

DuckDB is a modern open-source analytical database designed for fast OLAP workloads.
It is lightweight, cross-platform, and easy to embed inside Python notebooks and scripts.

DuckDB files (`.duckdb`) behave similarly to SQLite files (`.db`):
no server, no configuration, and everything runs in-process.

## Python

DuckDB integrates tightly with Python using the standard `duckdb` package.

```python
import duckdb

conn = duckdb.connect("data/warehouse/smart_sales.duckdb")
conn.execute("SELECT COUNT(*) FROM fact_sale").fetchall()
```

DuckDB can query Pandas DataFrames directly, join across CSVs, and write Parquet files.

---

## Power BI Desktop (Windows)

We can connect PowerBI to DuckDB using the **DuckDB ODBC Driver**.

1. Download it from: <https://duckdb.org/docs/api/odbc/overview>.
1. Install the 64-bit ODBC driver.
2. Create a Windows DSN (Data Source Name):
   1. Open Windows Start menu and type **ODBC Data Sources (64-bit)**
   2. Click the app when it appears to launch it
   3. Select the "System DSN" tab.
   4. Click Add… and choose **DuckDB ODBC Driver**
   5. Click Finish
   6. Name it SmartSalesDuckDB
   7. Click Browse… and select your file, for example:`data/warehouse/smart_sales.duckdb`

In PowerBI, select this DNS from **Get Data / ODBC**.

## Apache Spark

Apache Spark can connect to DuckDB using the **DuckDB JDBC Driver**.

1. Download the DuckDB JDBC `.jar` from:
   <https://github.com/duckdb/duckdb/releases>
2. Save the `.jar` file into your repo at: `lib/duckdb-jdbc.jar`
3. Configure Spark:

```python
spark = (
    SparkSession.builder
    .config("spark.driver.extraClassPath", "lib/duckdb-jdbc.jar")
    .getOrCreate()
)
```

1. Load a table:

```python
df = spark.read.format("jdbc").options(
    url="jdbc:duckdb:data/warehouse/smart_sales.duckdb",
    dbtable="fact_sale"
).load()
```


## OPTIONAL: DuckDB CLI (Command Line Interface)

This is not required.

DuckDB provides a simple, fast SQL shell for working with `.duckdb` files from the terminal.

To use it:

1. Download the CLI for your OS from: <https://duckdb.org/docs/installation/index>
2. Unzip the package
3. Add the unzipped folder to your PATH

Once installed, we can open a database from the terminal:

```shell
duckdb data/warehouse/smart_sales.duckdb
```

Once inside the shell:

```sql
.tables
SELECT COUNT(*) FROM fact_sale;
```

Learn more at: <https://duckdb.org/docs/sql/introduction.html>
