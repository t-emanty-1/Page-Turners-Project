"""Functions for visualising book data."""

import matplotlib.pyplot as plt


def plot_rating_distribution(books):
    """
    Create a histogram of average book ratings.

    Parameters
    ----------
    books : pandas.DataFrame
        Cleaned book dataset.

    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the histogram.
    """
    fig, ax = plt.subplots()

    ax.hist(books["average_rating"], bins=20, edgecolor="black")

    ax.set_title("Distribution of Average Book Ratings")
    ax.set_xlabel("Average Rating")
    ax.set_ylabel("Number of Books")

    fig.tight_layout()

    return fig