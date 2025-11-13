"""Data prep pipeline.

File: src/analytics_project/data_prep.py.
"""

# Imports go after the opening docstring

import pathlib

import pandas as pd

from .data_scrubber import DataScrubber
from .utils_logger import init_logger, logger, project_root

# Set up paths as constants
DATA_DIR: pathlib.Path = project_root.joinpath("data")
RAW_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("raw")


# Define a reusable function that accepts a full path.
def read_and_log(path: pathlib.Path) -> pd.DataFrame:
    """Read a CSV at the given path into a DataFrame, with friendly logging.

    We know reading a csv file can fail
    (the file might not exist, it could be corrupted),
    so we put the statement in a try block.
    It could fail due to a FileNotFoundError or other exceptions.
    If it succeeds, we log the shape of the DataFrame.
    If it fails, we log an error and return an empty DataFrame.
    """
    try:
        # Typically, we log the start of a file read operation
        logger.info(f"Reading raw data from {path}.")
        df = pd.read_csv(path)
        # Typically, we log the successful completion of a file read operation
        logger.info(
            f"{path.name}: loaded DataFrame with shape {df.shape[0]} rows x {df.shape[1]} cols"
        )
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Error reading {path}: {e}")
        return pd.DataFrame()


# Define a main function to start our data processing pipeline.


def main() -> None:
    """Process raw data."""
    logger.info("Starting data preparation...")

    # Build explicit paths for each file under data/raw
    customer_path: pathlib.Path = RAW_DATA_DIR.joinpath("customers_data.csv")
    product_path: pathlib.Path = RAW_DATA_DIR.joinpath("products_data.csv")
    sales_path: pathlib.Path = RAW_DATA_DIR.joinpath("sales_data.csv")

    # Read them all into a df we can pass in to the DataScrubber
    df_customers: pd.DataFrame = read_and_log(customer_path)

    if not df_customers.empty:
        scrubber = DataScrubber(df_customers)
        scrubber.remove_duplicate_records()
        df_customers = scrubber.handle_missing_data(fill_value="N/A")
        logger.info("Cleaned customers data.")

    # Can you extend this to read and clean the other files?
    # First, name a variable for what is returned by read_and_log
    # Then, create a DataScrubber instance for that df
    # Finally, call the methods to clean the data
    read_and_log(product_path)
    read_and_log(sales_path)

    # At the very end, log that we're done.
    logger.info("Data preparation complete.")


# Standard Python idiom to run this module as a script when executed directly.

if __name__ == "__main__":
    # Initialize logger
    init_logger()

    # Call the main function by adding () after the function name
    main()
