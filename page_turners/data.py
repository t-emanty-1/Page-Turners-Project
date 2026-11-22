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


def clean_books(books):
    """
    Prepare books for the ratings analysis.

    Parameters
    ----------
    books : pandas.DataFrame
        Original book dataset.

    Returns
    -------
    pandas.DataFrame
        Books with valid rating information.
    """
    cleaned_books = books.dropna(
        subset=["average_rating", "ratings_count"]
    ).copy()

    cleaned_books = cleaned_books[cleaned_books["ratings_count"] > 0]

    return cleaned_books