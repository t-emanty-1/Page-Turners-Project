import pandas as pd
import streamlit as st

st.title("Page Turners")

books = pd.read_csv("books.csv")

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

# Explore selected Latin American authors

st.subheader("Selected Latin American authors")

selected_authors = [
    "Isabel Allende",
    "Gabriel García Márquez",
    "Jorge Luis Borges",
    "Julio Cortázar",
    "Adolfo Bioy Casares",
]

# Count books for each author
author_counts = []

for author in selected_authors:
    matches = books["authors"].str.contains(
        author, case=False, na=False, regex=False
    )
    author_counts.append({
        "Author": author,
        "Books found": int(matches.sum())
    })

st.dataframe(pd.DataFrame(author_counts), hide_index=True)

# Select an author and display their books
chosen_author = st.selectbox(
    "Choose an author",
    selected_authors
)

chosen_books = books[
    books["authors"].str.contains(
        chosen_author, case=False, na=False, regex=False
    )
]

st.subheader("Books by " + chosen_author)

st.dataframe(
    chosen_books[
        ["title", "authors", "average_rating", "ratings_count"]
    ].sort_values("ratings_count", ascending=False),
    hide_index=True
)
