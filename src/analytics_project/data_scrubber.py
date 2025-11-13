"""data_scrubber.py.

Reusable utility class for performing common data cleaning and
preparation tasks on a pandas DataFrame.

This class provides methods for:
- Checking data consistency
- Removing duplicates
- Handling missing values
- Filtering outliers
- Renaming and reordering columns
- Formatting strings
- Parsing date fields

Use this class to perform similar cleaning operations across multiple files.
You are not required to use this class, but it shows how we can organize
reusable data cleaning logic - or you can use the logic examples in your own code.

Example:
    from .data_scrubber import DataScrubber
    scrubber = DataScrubber(df)
    df = scrubber.remove_duplicate_records().handle_missing_data(fill_value="N/A")

"""

import io

import pandas as pd


class DataScrubber:
    """A utility class for performing common data cleaning and preparation tasks on pandas DataFrames.

    This class provides methods for checking data consistency, removing duplicates,
    handling missing values, filtering outliers, renaming and reordering columns,
    formatting strings, and parsing date fields.

    Attributes
    ----------
    df : pd.DataFrame
        The DataFrame to be scrubbed and cleaned.

    Methods
    -------
    check_data_consistency_before_cleaning() -> dict
        Check data consistency before cleaning by calculating counts of null and duplicate entries.
    check_data_consistency_after_cleaning() -> dict
        Check data consistency after cleaning to ensure there are no null or duplicate entries.
    remove_duplicate_records() -> pd.DataFrame
        Remove duplicate rows from the DataFrame.
    handle_missing_data(drop: bool = False, fill_value = None) -> pd.DataFrame
        Handle missing data in the DataFrame by dropping or filling values.
    """

    def __init__(self, df: pd.DataFrame):
        """Initialize the DataScrubber with a DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to be scrubbed.
        """
        self.df = df

    def check_data_consistency_before_cleaning(self) -> dict[str, pd.Series | int]:
        """Check data consistency before cleaning by calculating counts of null and duplicate entries.

        Returns:
            dict: Dictionary with counts of null values and duplicate rows.
        """
        null_counts = self.df.isnull().sum()
        duplicate_count = self.df.duplicated().sum()
        return {"null_counts": null_counts, "duplicate_count": duplicate_count}

    def check_data_consistency_after_cleaning(self) -> dict[str, pd.Series | int]:
        """Check data consistency after cleaning to ensure there are no null or duplicate entries.

        Returns:
            dict: Dictionary with counts of null values and duplicate rows, expected to be zero for each.
        """
        null_counts = self.df.isnull().sum()
        duplicate_count = self.df.duplicated().sum()
        assert null_counts.sum() == 0, "Data still contains null values after cleaning."
        assert duplicate_count == 0, "Data still contains duplicate records after cleaning."
        return {"null_counts": null_counts, "duplicate_count": duplicate_count}

    def convert_column_to_new_data_type(self, column: str, new_type: type) -> pd.DataFrame:
        """Convert a specified column to a new data type.

        Args:
            column: Name of the column to convert.
            new_type: The target data type (e.g., 'int', 'float', 'str').

        Returns:
            pd.DataFrame: Updated DataFrame with the column type converted.

        Raises:
            ValueError: If the specified column not found in the DataFrame.
        """
        try:
            self.df[column] = self.df[column].astype(new_type)
            return self.df
        except KeyError as exc:
            raise ValueError(f"Column name '{column}' not found in the DataFrame.") from exc

    def drop_columns(self, columns: list[str]) -> pd.DataFrame:
        """Drop specified columns from the DataFrame.

        Parameters
        ----------
        columns : list[str]
            List of column names to drop.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with specified columns removed.

        Raises
        ------
            ValueError: If a specified column is not found in the DataFrame.
        """
        for column in columns:
            if column not in self.df.columns:
                raise ValueError(f"Column name '{column}' not found in the DataFrame.")
        self.df = self.df.drop(columns=columns)
        return self.df

    def filter_column_outliers(
        self, column: str, lower_bound: float | int, upper_bound: float | int
    ) -> pd.DataFrame:
        """Filter outliers in a specified column based on lower and upper bounds.

        Args:
            column: Name of the column to filter for outliers.
            lower_bound: Lower threshold for outlier filtering.
            upper_bound: Upper threshold for outlier filtering.

        Returns:
            pd.DataFrame: Updated DataFrame with outliers filtered out.

        Raises:
            ValueError: If the specified column not found in the DataFrame.
        """
        try:
            self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
            return self.df
        except KeyError as exc:
            raise ValueError(f"Column name '{column}' not found in the DataFrame.") from exc

    def format_column_strings_to_lower_and_trim(self, column: str) -> pd.DataFrame:
        """Format strings in a specified column by converting to lowercase and trimming whitespace.

        Parameters
        ----------
        column : str
            Name of the column to format.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with formatted string column.

        Raises
        ------
            ValueError: If the specified column not found in the DataFrame.
        """
        try:
            self.df[column] = self.df[column].str.lower().str.strip()
            return self.df
        except KeyError as exc:
            raise ValueError(f"Column name '{column}' not found in the DataFrame.") from exc

    def format_column_strings_to_upper_and_trim(self, column: str) -> pd.DataFrame:
        """Format strings in a specified column by converting to uppercase and trimming whitespace.

        Parameters
        ----------
        column : str
            Name of the column to format.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with formatted string column.

        Raises
        ------
            ValueError: If the specified column not found in the DataFrame.
        """
        try:
            # TODO: Fix the following logic to call str.upper() and str.strip() on the given column
            # HINT: See previous function for an example
            self.df[column] = self.df[column]
            return self.df
        except KeyError as exc:
            raise ValueError(f"Column name '{column}' not found in the DataFrame.") from exc

    def handle_missing_data(
        self, drop: bool = False, fill_value: None | float | int | str = None
    ) -> pd.DataFrame:
        """Handle missing data in the DataFrame.

        Parameters
        ----------
        drop : bool, optional
            If True, drop rows with missing values. Default is False.
        fill_value : None | float | int | str, optional
            Value to fill in for missing entries if drop is False.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with missing data handled.
        """
        if drop:
            self.df = self.df.dropna()
        elif fill_value is not None:
            self.df = self.df.fillna(fill_value)
        return self.df

    def inspect_data(self) -> tuple[str, str]:
        """Inspect the data by providing DataFrame information and summary statistics.

        Returns:
            tuple: (info_str, describe_str), where `info_str` is a string representation of DataFrame.info()
                   and `describe_str` is a string representation of DataFrame.describe().
        """
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        info_str = buffer.getvalue()  # Retrieve the string content of the buffer

        # Capture the describe output as a string
        describe_str = (
            self.df.describe().to_string()
        )  # Convert DataFrame.describe() output to a string
        return info_str, describe_str

    def parse_dates_to_add_standard_datetime(self, column: str) -> pd.DataFrame:
        """Parse a specified column as datetime format and add it as a new column named 'StandardDateTime'.

        Parameters
        ----------
        column : str
            Name of the column to parse as datetime.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with a new 'StandardDateTime' column containing parsed datetime values.

        Raises
        ------
            ValueError: If the specified column not found in the DataFrame.
        """
        try:
            self.df["StandardDateTime"] = pd.to_datetime(self.df[column])
            return self.df
        except KeyError as exc:
            raise ValueError(f"Column name '{column}' not found in the DataFrame.") from exc

    def remove_duplicate_records(self) -> pd.DataFrame:
        """Remove duplicate rows from the DataFrame.

        Returns:
            pd.DataFrame: Updated DataFrame with duplicates removed.

        """
        self.df = self.df.drop_duplicates()
        return self.df

    def rename_columns(self, column_mapping: dict[str, str]) -> pd.DataFrame:
        """Rename columns in the DataFrame based on a provided mapping.

        Parameters
        ----------
        column_mapping : dict[str, str]
            Dictionary where keys are old column names and values are new names.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with renamed columns.

        Raises
        ------
            ValueError: If a specified column is not found in the DataFrame.
        """
        for old_name, _new_name in column_mapping.items():
            if old_name not in self.df.columns:
                raise ValueError(f"Column '{old_name}' not found in the DataFrame.")

        self.df = self.df.rename(columns=column_mapping)
        return self.df

    def reorder_columns(self, columns: list[str]) -> pd.DataFrame:
        """Reorder columns in the DataFrame based on the specified order.

        Parameters
        ----------
        columns : list[str]
            List of column names in the desired order.

        Returns
        -------
            pd.DataFrame: Updated DataFrame with reordered columns.

        Raises
        ------
            ValueError: If a specified column is not found in the DataFrame.
        """
        for column in columns:
            if column not in self.df.columns:
                raise ValueError(f"Column name '{column}' not found in the DataFrame.")
        self.df = self.df[columns]
        return self.df
