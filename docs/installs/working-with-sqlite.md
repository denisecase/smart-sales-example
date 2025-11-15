# Working with SQLite

> Using SQLite with Python, Power BI, and Spark SQL

SQLite is lightweight, cross-platform, and already included with Python. It is a file-based relational data store so we don't need to install and configure services like would be needed with MySQL, SQLServer, or other enterprise solution.

It makes an accessible proxy to learn about working with data warehouses.

## Python

Python includes SQLite support by default through the built-in `sqlite3` module.

Just import the package from the Python Standard Library in your Python code file or notebook:

```python
import sqlite3

conn = sqlite3.connect("data/warehouse/smart_sales.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM fact_sale")
```

## Power BI Desktop (Windows)

We can connect PowerBI to SQLite using the **SQLite ODBC driver**.

1. Download it from <https://www.ch-werner.de/sqliteodbc>.
2. Install the **SQLite3 ODBC Driver (64-bit)** using default settings.
3. Create a Windows DSN (Data Source Name):
   1. Open Windows Start menu and type **ODBC Data Sources (64-bit)**
   2. Click the app when it appears to launch it
   3. Select the "System DSN" tab.
   4. Click Add… and choose **SQLite3 ODBC Driver**
   5. Click Finish
   6. Name it SmartSalesDSN
   7. Click Browse… and select your file, for example: `data/warehouse/smart_sales.db`

In PowerBI, select this DNS from **Get Data / ODBC**.

## Apache Spark

Apache Spark can connect to SQLite using the **SQLite JDBC Driver**.

1. Download the SQLite JDBC `.jar` from <https://github.com/xerial/sqlite-jdbc/releases>
2. Save the `.jar` file into your repo at: `lib/sqlite-jdbc.jar`
3. Configure PySpark:

```python
spark = (
    SparkSession.builder
    .config("spark.driver.extraClassPath", "lib/sqlite-jdbc.jar")
    .getOrCreate()
)
```

4. Load a table:

```python
df = spark.read.format("jdbc").options(
    url="jdbc:sqlite:data/warehouse/smart_sales.db",
    dbtable="fact_sale"
).load()
```

## OPTIONAL: SQLite CLI (Command Line Interface)

This is not required.

SQLite provides a simple, fast SQL shell for working with `.db` files from the terminal.

To use it:

1. Download the CLI from <https://sqlite.org/download.html> (look for `sqlite-tools` for your OS)
2. Unzip the package
3. Add the unzipped folder to your PATH.

Once installed, we can open a database from the terminal:

```shell
sqlite3 data/warehouse/smart_sales.db
```

Once inside the shell:

```sql
.tables
SELECT COUNT(*) FROM fact_sale;
```

Learn more at: <https://sqlite.org/cli.html>
