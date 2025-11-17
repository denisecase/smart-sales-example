"""Module 6: OLAP Goal Script (uses cubed results).

File: src/analytics_project/olap/goal_sales_by_day.py.

Module: analytics_project.olap.goal_sales_by_day

This script uses our precomputed cubed data set to get the information
we need to answer a specific business goal.

GOAL: Analyze sales data to determine which day of the week
consistently shows the lowest sales revenue.

ACTION: This can help inform decisions about reducing operating hours
or focusing marketing efforts on less profitable days.

PROCESS:
Group transactions by the day of the week.
Sum SaleAmount for each day.
Identify the day with the lowest total revenue.

This example assumes a cube data set with the following column names (yours will differ).
DayOfWeek,product_id,customer_id,sale_amount_sum,sale_amount_mean,sale_id_count,sale_ids
Friday,101,1001,6344.96,6344.96,1,[582]
etc.
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


def analyze_sales_by_weekday(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by DayOfWeek."""
    try:
        # Group by DayOfWeek and sum the sales
        sales_by_weekday = cube_df.groupby("DayOfWeek")["sale_amount_sum"].sum().reset_index()
        sales_by_weekday.rename(columns={"sale_amount_sum": "TotalSales"}, inplace=True)
        sales_by_weekday.sort_values(by="TotalSales", inplace=True)
        logger.info("Sales aggregated by DayOfWeek successfully.")
        return sales_by_weekday
    except Exception as e:
        logger.error(f"Error analyzing sales by DayOfWeek: {e}")
        raise


def identify_least_profitable_day(sales_by_weekday: pd.DataFrame) -> str:
    """Identify the day with the lowest total sales revenue."""
    try:
        least_profitable_day = sales_by_weekday.iloc[0]
        logger.info(
            f"Least profitable day: {least_profitable_day['DayOfWeek']} with revenue ${least_profitable_day['TotalSales']:.2f}."
        )
        return least_profitable_day["DayOfWeek"]
    except Exception as e:
        logger.error(f"Error identifying least profitable day: {e}")
        raise


def visualize_sales_by_weekday(sales_by_weekday: pd.DataFrame) -> None:
    """Visualize total sales by day of the week."""
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(
            sales_by_weekday["DayOfWeek"],
            sales_by_weekday["TotalSales"],
            color="skyblue",
        )
        plt.title("Total Sales by Day of the Week", fontsize=16)
        plt.xlabel("Day of the Week", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_day_of_week.png")
        plt.savefig(output_path)
        logger.info(f"Visualization saved to {output_path}.")
        plt.show()
    except Exception as e:
        logger.error(f"Error visualizing sales by day of the week: {e}")
        raise


def main():
    """Analyze and visualize sales data."""
    logger.info("Starting SALES_LOW_REVENUE_DAYOFWEEK analysis...")

    # Step 1: Load the precomputed OLAP cube
    cube_df = load_olap_cube(CUBED_FILE)

    # Step 2: Analyze total sales by DayOfWeek
    sales_by_weekday = analyze_sales_by_weekday(cube_df)

    # Step 3: Identify the least profitable day
    least_profitable_day = identify_least_profitable_day(sales_by_weekday)
    logger.info(f"Least profitable day: {least_profitable_day}")
    logger.info("Close the Figure to complete this script.")

    # Step 4: Visualize total sales by DayOfWeek
    visualize_sales_by_weekday(sales_by_weekday)
    logger.info("Analysis and visualization completed successfully.")


if __name__ == "__main__":
    main()
