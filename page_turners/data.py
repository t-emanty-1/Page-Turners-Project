"""Functions for loading the book dataset."""

import pandas as pd


def load_books(csv_path="books.csv"):
    """
    Load book data from a CSV file.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the book data.
    """
    return pd.read_csv(csv_path)