import streamlit as st

from page_turners.analysis import (
    calculate_rating_correlation,
    summarize_ratings_by_decade,
)
from page_turners.data import load_books, clean_books
from page_turners.plots import plot_rating_distribution, plot_popularity_vs_rating

st.title("Page Turners")

st.write("Exploring book popularity and reader appreciation.")

st.header("About the Project")

st.write(
    "This project explores the goodbooks-10k dataset "
    "to investigate book ratings, popularity and publication years."
)

st.markdown(
    "**Main research question:** Do books with more ratings "
    "tend to have higher average scores?"
)

st.write(
    "The analysis also examines the distribution of average "
    "ratings and compares ratings across publication decades."
)


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

st.header("Dataset Overview")

st.write("Source: goodbooks-10k")

col1, col2 = st.columns(2)

col1.metric("Books in dataset", len(books))
col2.metric("Books analysed", len(cleaned_books))

st.header("1. Distribution of Average Ratings")

figure = plot_rating_distribution(cleaned_books)

for ax in figure.axes:
    for patch in ax.patches:
        patch.set_facecolor(dark_purple)

st.pyplot(figure)

st.write(
    "Most books in the dataset have average ratings close to 4 out of 5. "
    "Very low and very high average ratings are less common."
)

st.caption(
    "Each bar represents the number of books within "
    "a particular average rating interval."
)


correlation = calculate_rating_correlation(cleaned_books)

st.header("2. Popularity and Average Ratings")
st.write("Pearson correlation coefficient:", round(correlation, 4))

scatter_figure = plot_popularity_vs_rating(cleaned_books)

for ax in scatter_figure.axes:
    for collection in ax.collections:
        collection.set_color(dark_purple)

st.pyplot(scatter_figure)

st.write(
    "The scatter plot shows no clear linear relationship between "
    "the number of ratings and the average book rating."
)

st.write(
    f"The Pearson correlation coefficient of {correlation:.3f} "
    "indicates a very weak positive linear relationship. "
    "More ratings do not necessarily correspond to higher average scores."
)

st.caption(
    "Each point represents one book. The horizontal axis uses "
    "a logarithmic scale because the number of ratings varies considerably."
)


st.header("3. Average Ratings by Publication Decade")

decade_summary = summarize_ratings_by_decade(cleaned_books)

recent_decades = decade_summary[decade_summary["decade"] >= 1950]


st.dataframe(
    recent_decades,
    hide_index=True,
    column_config={
        "decade": st.column_config.NumberColumn(
            "Decade", format="%d"
        ),
        "book_count": "Books",
        "mean_rating": st.column_config.NumberColumn(
            "Mean rating", format="%.3f"
        ),
    },
)


st.write(
    "Mean book ratings remain relatively similar across publication "
    "decades, with values close to 4 out of 5."
)

st.write(
    "Books published in the 1960s have the highest mean rating "
    "among the displayed decades, while those published in the "
    "2000s have the lowest. However, the differences are small."
)

st.caption(
    "The comparison focuses on decades from 1950 onwards "
    "because earlier decades generally contain fewer books. "
    "Each book contributes equally to the mean rating."
)

st.header("Conclusion")

st.write(
    "The analysis shows that most books in the dataset have "
    "average ratings close to 4 out of 5."
)

st.write(
    "Book popularity, measured by the number of ratings, "
    "has a very weak positive linear relationship with average rating."
)

st.write(
    "The comparison across publication decades also reveals "
    "relatively small differences in mean book ratings."
)

st.subheader("Limitations")

st.write(
    "- The dataset does not represent all published books.\n"
    "- The number of ratings is only one measure of popularity.\n"
    "- Correlation does not imply causation.\n"
    "- The number of books varies considerably between decades.\n"
    "- The analysis is descriptive and does not establish "
    "statistical significance."
)

with st.expander("Dataset Inspection and Data Quality"):
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
