
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
