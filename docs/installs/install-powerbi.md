# Installing Power BI Desktop (Windows)

> Power BI Desktop is a free reporting tool for creating dashboards and interactive visualizations.

## 1. Install Power BI Desktop

Download from the official site: <https://powerbi.microsoft.com/downloads>

Choose **Power BI Desktop (64-bit)**.


## 2. Install the ODBC Driver

Power BI needs an ODBC driver to read SQLite or DuckDB databases.

Install the ODBC (Open Database Connectivity) driver and create a **Data Name Source**:

- If using SQLite, see [Working with SQLite](./working-with-sqlite.md)
- If using DuckDB, see [Working with DuckDB](./working-with-duckdb.md)


## 3. Configure PowerBI to Use the ODBC Driver

1. Open Power BI Desktop
2. Click **Get Data / ODBC**
3. Select the DSN you created


## 4. Use PowerBI to Access Tables

1. Load your dimension and fact tables


## Optional Video

Optional Video: How to Connect Power BI with SQLite Database and Import Data (6 minutes)

https://www.youtube.com/watch?v=v9OG5Ry5zDU
