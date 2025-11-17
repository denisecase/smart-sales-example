"""Module 6: OLAP Goal Script (uses cubed results).

File: src/analytics_project/olap/goal_top_product_by_day.py.

Module: analytics_project.olap.goal_top_product_by_day

This script uses our precomputed cubed data set to get the information
we need to answer a specific business goal.

GOAL: Analyze sales data to determine the product with the highest revenue
for each day of the week.

ACTION: This can help inform inventory decisions, optimize promotions,
and understand purchasing patterns on different days.

PROCESS:
Group transactions by the day of the week and product.
Sum SaleAmount for each product on each day.
Identify the top product for each day based on total revenue.

DayOfWeek,product_id,customer_id,sale_amountd_sum,sale_amount_mean,sale_id_count,sale_ids
Friday,101,1001,6344.96,6344.96,1,[582]
"""

import pathlib

import matplotlib.pyplot as plt
import pandas as pd

from analytics_project.utils_logger import logger

# Global constants for paths and key directories

THIS_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent
DW_DIR: pathlib.Path = THIS_DIR  # src/analytics_project/olap/
PACKAGE_DIR: pathlib.Path = DW_DIR.parent  # src/analytics_project/
SRC_DIR: pathlib.Path = PACKAGE_DIR.parent  # src/
PROJECT_ROOT_DIR: pathlib.Path = SRC_DIR.parent  # project_root/

# Data directories
DATA_DIR: pathlib.Path = PROJECT_ROOT_DIR / "data"
WAREHOUSE_DIR: pathlib.Path = DATA_DIR / "warehouse"

# Warehouse database location (SQLite)
DB_PATH: pathlib.Path = WAREHOUSE_DIR / "smart_sales.db"

# OLAP output directory
OLAP_OUTPUT_DIR: pathlib.Path = DATA_DIR / "olap_cubing_outputs"

# CUBED File path
CUBED_FILE: pathlib.Path = OLAP_OUTPUT_DIR / "multidimensional_olap_cube.csv"

# Results output directory
RESULTS_OUTPUT_DIR: pathlib.Path = DATA_DIR / "results"

# Recommended - log paths and key directories for debugging

logger.info(f"THIS_DIR:            {THIS_DIR}")
logger.info(f"DW_DIR:              {DW_DIR}")
logger.info(f"PACKAGE_DIR:         {PACKAGE_DIR}")
logger.info(f"SRC_DIR:             {SRC_DIR}")
logger.info(f"PROJECT_ROOT_DIR:    {PROJECT_ROOT_DIR}")

logger.info(f"DATA_DIR:            {DATA_DIR}")
logger.info(f"WAREHOUSE_DIR:       {WAREHOUSE_DIR}")
logger.info(f"DB_PATH:             {DB_PATH}")
logger.info(f"OLAP_OUTPUT_DIR:     {OLAP_OUTPUT_DIR}")
logger.info(f"RESULTS_OUTPUT_DIR:  {RESULTS_OUTPUT_DIR}")

# Create output directory if it does not exist
OLAP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Create output directory for results if it doesn't exist
RESULTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_olap_cube(file_path: pathlib.Path) -> pd.DataFrame:
    """Load the precomputed OLAP cube data."""
    try:
        cube_df = pd.read_csv(file_path)
        logger.info(f"OLAP cube data successfully loaded from {file_path}.")
        return cube_df
    except Exception as e:
        logger.error(f"Error loading OLAP cube data: {e}")
        raise


def analyze_top_product_by_weekday(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Identify the product with the highest revenue for each day of the week."""
    try:
        # Group by DayOfWeek and product_id, sum the sales
        grouped = (
            cube_df.groupby(["DayOfWeek", "product_id"])["sale_amount_sum"].sum().reset_index()
        )
        grouped.rename(columns={"sale_amount_sum": "TotalSales"}, inplace=True)

        # Sort within each day to find the top product
        top_products = (
            grouped.sort_values(["DayOfWeek", "TotalSales"], ascending=[True, False])
            .groupby("DayOfWeek")
            .head(1)
        )
        logger.info("Top products identified for each day of the week.")
        return top_products
    except Exception as e:
        logger.error(f"Error analyzing top product by DayOfWeek: {e}")
        raise


def visualize_sales_by_weekday_and_product(cube_df: pd.DataFrame) -> None:
    """Visualize total sales by day of the week, broken down by product."""
    try:
        # Pivot the data to organize sales by DayOfWeek and ProductID
        sales_pivot = cube_df.pivot_table(
            index="DayOfWeek",
            columns="product_id",
            values="sale_amount_sum",
            aggfunc="sum",
            fill_value=0,
        )

        # Plot the stacked bar chart
        sales_pivot.plot(kind="bar", stacked=True, figsize=(12, 8), colormap="tab10")

        plt.title("Total Sales by Day of the Week and Product", fontsize=16)
        plt.xlabel("Day of the Week", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title="Product ID", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_day_and_product.png")
        plt.savefig(output_path)
        logger.info(f"Stacked bar chart saved to {output_path}.")
        plt.show()
    except Exception as e:
        logger.error(f"Error visualizing sales by day and product: {e}")
        raise


def main():
    """Analyze and visualize top product sales by day of the week."""
    logger.info("Starting SALES_TOP_PRODUCT_BY_WEEKDAY analysis...")

    # Step 1: Load the precomputed OLAP cube
    cube_df = load_olap_cube(CUBED_FILE)

    # Step 2: Analyze top products by DayOfWeek
    top_products = analyze_top_product_by_weekday(cube_df)
    print(top_products)

    # Step 3: Visualize the results
    visualize_sales_by_weekday_and_product(cube_df)
    logger.info("Analysis and visualization completed successfully.")


if __name__ == "__main__":
    main()
