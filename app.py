import streamlit as st

from page_turners.analysis import (
    calculate_rating_correlation,
    summarize_ratings_by_decade,
)
from page_turners.data import load_books, clean_books
from page_turners.plots import plot_rating_distribution, plot_popularity_vs_rating

st.title("Page Turners")

dark_purple = "#A15AD3"

try:
    books = load_books()
except FileNotFoundError:
    st.error("Could not find books.csv. Make sure the dataset is in the project folder.")
    st.stop()

required_columns = [
    "book_id",
    "title",
    "authors",
    "original_publication_year",
    "average_rating",
    "ratings_count",
]

missing_columns = [
    column for column in required_columns if column not in books.columns
]

st.subheader("Required columns")

if missing_columns:
    st.error("Missing required columns: " + ", ".join(missing_columns))
    st.stop()
else:
    st.success("All required columns are present.")

cleaned_books = clean_books(books)

st.write("Books available for ratings analysis:", len(cleaned_books))
correlation = calculate_rating_correlation(cleaned_books)

st.subheader("Popularity and Average Ratings")
st.write("Pearson correlation coefficient:", round(correlation, 4))

st.subheader("Distribution of Average Ratings")

figure = plot_rating_distribution(cleaned_books)

for ax in figure.axes:
    for patch in ax.patches:
        patch.set_facecolor(dark_purple)

st.pyplot(figure)

st.subheader("Popularity vs Average Rating")

scatter_figure = plot_popularity_vs_rating(cleaned_books)

for ax in scatter_figure.axes:
    for collection in ax.collections:
        collection.set_color(dark_purple)

st.pyplot(scatter_figure)

st.subheader("Average Ratings by Publication Decade")

decade_summary = summarize_ratings_by_decade(cleaned_books)

recent_decades = decade_summary[decade_summary["decade"] >= 1950]

st.dataframe(recent_decades, hide_index=True)

st.subheader("Preview of the book data")
st.dataframe(books.head())

st.subheader("Dataset size")
st.write("Number of rows:", books.shape[0])
st.write("Number of columns:", books.shape[1])

st.subheader("Missing values in each column")
st.dataframe(books.isna().sum())

st.subheader("Column data types")
st.dataframe(books.dtypes.astype(str))

st.subheader("Duplicate book IDs")
st.write(books["book_id"].duplicated().sum())

st.subheader("Numerical summary")

summary_columns = [
    "original_publication_year",
    "average_rating",
    "ratings_count",
]

st.dataframe(books[summary_columns].describe())

st.subheader("Oldest books")

year_columns = ["title", "authors", "original_publication_year"]

st.dataframe(
    books.sort_values("original_publication_year")[year_columns].head(10)
)

st.subheader("Books with missing publication years")
missing_year = books["original_publication_year"].isna()

st.dataframe(books.loc[missing_year, year_columns])
