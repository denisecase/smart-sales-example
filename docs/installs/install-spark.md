# Installing Apache Spark

> Apache Spark is a distributed computing engine used for large-scale data processing and analytics.

## 0. ADVANCED FOR WINDOWS USERS (OPTIONAL)

Apache Spark is optional for Windows users.

If you want to run Spark on Windows, you must set up **WSL (Ubuntu)** and make a **second clone** of your project _inside WSL_.
There will be two _operating system specfic_ versions of the project:

- **Windows repo** with **Power BI**
- **WSL repo** with **Spark**

Steps:

1. Open **WSL** (Ubuntu) and make a second clone of your repo **from inside WSL**, for example:
   `git clone https://github.com/...`
2. In Windows, install the **"WSL – Windows Subsystem for Linux"** extension (`ms-vscode-remote.remote-wsl`) in VS Code.
3. In WSL, navigate into the project folder and run: `code .` This opens the WSL project in VS Code.
4. All notebooks, Spark sessions, and terminal commands will now run **inside WSL**, while the VS Code interface runs normally in Windows.

All of the following steps should be run inside a **WSL bash terminal**.

## 1. Install Apache Spark

Download Spark from: <https://spark.apache.org/downloads.html>

Choose:

- Spark version: 3.x
- Package type: **Pre-built for Apache Hadoop**
- Follow install instructions for your OS

Add Spark’s `bin/` folder to your shell PATH.

Example:

```bash
export PATH="$PATH:/path/to/spark/bin"
```

By default, the project **comments out** `pyspark` in `pyproject.toml`.

1. Open `pyproject.toml`.
2. Uncomment the `pyspark` line in the dependencies section
3. Resync your environment:

```bash
uv sync --extra dev --extra docs --upgrade
```

This ensures:

- `pyspark` is installed
- Jupyter notebooks can import `pyspark`
- Your Spark session (`SparkSession.builder`) works inside the notebook

---

## 2. Install the JDBC Driver

Spark needs a JDBC driver to read SQLite or DuckDB databases.

Install the JDBC (Java Database Connectivity) driver and create a **Data Name Source**:

- If using SQLite, see [Working with SQLite](./working-with-sqlite.md)
- If using DuckDB, see [Working with DuckDB](./working-with-duckdb.md)

---

## 3. Configure Spark to Use the JDBC Driver

Example PySpark config:

```python
spark = (
    SparkSession.builder
    .appName("SmartSales")
    .config("spark.driver.extraClassPath", "lib/sqlite-jdbc.jar")
    .getOrCreate()
)
```

If Spark cannot find the driver, use an **absolute path**.

Restart the notebook kernel after updating Spark configuration.

## 4. Test Spark in a Notebook

```python
df = spark.read.format("jdbc").options(
    url="jdbc:sqlite:data/warehouse/smart_sales.db",
    dbtable="fact_sale"
).load()

df.show()
```
