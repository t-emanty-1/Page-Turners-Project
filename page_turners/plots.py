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


def plot_popularity_vs_rating(books):
    """
    Create a scatter plot of book popularity and average ratings.

    Parameters
    ----------
    books : pandas.DataFrame
        Cleaned book dataset.

    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the scatter plot.
    """
    fig, ax = plt.subplots()

    ax.scatter(
        books["ratings_count"],
        books["average_rating"],
        s=8,
        alpha=0.3
    )

    ax.set_xscale("log")

    ax.set_title("Book Popularity vs Average Rating")
    ax.set_xlabel("Number of Ratings (log scale)")
    ax.set_ylabel("Average Rating")

    fig.tight_layout()

    return fig