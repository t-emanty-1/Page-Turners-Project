"""Statistical calculations for book ratings."""

import numpy as np


def calculate_rating_correlation(books):
    """
    Calculate the correlation between rating counts and average ratings.

    Parameters
    ----------
    books : pandas.DataFrame
        Cleaned dataset containing book ratings.

    Returns
    -------
    float
        Pearson correlation coefficient.
    """
    rating_counts = books["ratings_count"].to_numpy()
    average_ratings = books["average_rating"].to_numpy()

    correlation = np.corrcoef(rating_counts, average_ratings)[0, 1]

    return float(correlation)


def summarize_ratings_by_decade(books):
    """
    Calculate the number of books and mean rating by decade.

    Parameters
    ----------
    books : pandas.DataFrame
        Cleaned book dataset.

    Returns
    -------
    pandas.DataFrame
        Summary of book counts and mean ratings by decade.
    """
    dated_books = books.dropna(subset=["original_publication_year"]).copy()

    dated_books = dated_books[dated_books["original_publication_year"] > 0].copy()

    dated_books["decade"] = (
        dated_books["original_publication_year"] // 10 * 10
    ).astype(int)

    summary = (
        dated_books.groupby("decade")
        .agg(
            book_count=("book_id", "size"),
            mean_rating=("average_rating", "mean"),
        )
        .reset_index()
    )

    return summary
