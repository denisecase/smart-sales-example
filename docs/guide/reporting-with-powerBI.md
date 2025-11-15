# Reporting with PowerBI

> Analyze and visualize stored data to generate business intelligence insights
> Common BI workflow: Connect / Load / Query / Explore / Visualize

Power BI connects to a warehouse using ODBC.
We must install **Power BI Desktop** and create a **DSN** (Data Source Name) before we can begin reporting.

## Task 1: Set Up PowerBI

Use Power BI Desktop and an **ODBC connection** to read data from a database.

See the instructions at [Install PowerBI](../installs/install-powerbi.md) and follow the steps to install an **ODBC driver** and configure the PowerBI **DSN**.

A short 6-minute video on "How to Connect Power BI with SQLite Database and Import Data" is linked on that page.

## Task 2: Load DW Tables into PowerBI

Start a project by loading the associated tables into PowerBI.

1. Open **Power BI Desktop**
2. Click **Get Data / ODBC**
3. Select the **DSN** created earlier (e.g., `SmartSalesDSN`)
4. Click **OK**. Power BI will show a list of available tables
5. Select all the tables you want to analyze:
   - Customer table
   - Product table
   - Sales table
6. Click **Load** to bring the tables into Power BI
7. Switch to **Model view** (left panel) to see how the tables are connected

## Task 3: Query & Aggregate Data

Use Power BI **Advanced Editor** to write a custom SQL queries.

1. In the Home tab, click **Transform Data** to open Power Query Editor.
2. In Power Query, click **Advanced Editor** (top menu).
3. Delete any existing code and replace it with a new SQL query (example below).
4. **IMPORTANT:** You must use your DSN name, table names, and column names for the SQL to work.

```shell
let
   source = ODBC.Query("dsn=smartsalesDSN",
      "SELECT c.name, SUM(s.amount) AS total_spent
      FROM sale s
      JOIN customer c ON s.customer_id = c.customer_id
      GROUP BY c.name
      ORDER BY total_spent DESC;")
in
   source
```

When done:

1. Click **Done**.
2. Rename the new query (on the left) to something like "Top Customers" that reflects your focus.
3. Click **Close & Apply** (upper left) to return to Report view.
4. This table can now be used in visuals (e.g., a bar chart).

## Task 4: Slice, Dice, and Drilldown

Implement slicing, dicing, and drilldown to analyze sales.

- **Slicing**: Add a date range slicer
- **Dicing:** Group data by two categorical dimensions
- **Drilldown**: Aggregate sales by Year > Quarter > Month

### 4a. Slicing in Power BI (by Date)

SQLite doesn't have true date types, so we use Power BI's **Transform Data** to extract parts of the date for slicing, dicing, and drilldown.

1. Click Transform Data to open Power Query.
2. Select the `sales` table.
3. Select the `order_date` column (or any "date-related" field).
4. On the top menu, click Add Column > Date > Year.
5. Then click Add Column > Date > Quarter.
6. Then click Add Column > Date > Month > Name of Month.
7. Click Close & Apply to save changes and return to the report view.
8. Return to Report view (center icon on the left).
9. From the Visualizations pane, click on the Slicer icon.
10. Drag a date field into the slicer.
11. If it doesn't show a range, click the dropdown (upper-right corner of slicer) and select **Between** to enable a date range slider.

### 4b. Dicing in Power BI (by Product Attributes)

To analyze two categorical dimensions, for example, to explore sales by product attributes (e.g. category and region or other characteristics), create a **Matrix** visual in Power BI.

1. Go to Report view.
2. From the Visualizations pane, click the Matrix visual to insert a Matrix.
3. Drag your first product attribute (e.g. category) to the **Rows** field well.
4. Drag your first product attribute (e.g. region) to the **Columns** field well.
5. Drag a numeric field to the **Values** field well.
6. Format  numeric values by using the column dropdown in the Values area.

This matrix help us dice the data and break it down by two categorical dimensions: e.g., product and region.

### 4c. Drilldown in Power BI (Year > Quarter > Month)

To explore sales over time, we'll use a column or line chart and enable drilldown so we can click into sales by year, quarter, and month.

1. Go to Report view.
2. From the Visualizations pane, click on either the Clustered **Column Chart** or **Line Chart**.
3. Drag hierarchy fields to the X-Axis or Axis field in order:
    1. order_year
    2. order_quarter
    3. order_month
4. Drag your numeric value (e.g., total amount) to Values area.
5. At the top left of the chart, click the drilldown arrow icon (a split-down arrow) to enable Drilldown.
6. Click on a bar or line point in the chart to drill down from Year > Quarter > Month.
7. Use the **up arrow** to move back up the hierarchy.

If nothing happens when clicking, make sure the chart supports hierarchy and the drilldown mode is active (look for the split arrow).

## Task 5: Create Visuals

Create visuals to interpret results.

Common charts:

- Create a bar chart for **Top Customers** (or similar)
- Create a line chart for **Sales Trends** (or similar trend)
- Add a slicer for product categories (or other categorical field)

To create visuals:

1. Go to Report View.
2. Use the **Visualizations** pane to choose a chart (e.g., Bar, Line).
3. Drag fields into the chart (e.g., customer name to Axis, total spent to Values).
4. Use **Slicers** to filter by category, region, or date if you've added those earlier.
