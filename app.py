import pandas as pd
import streamlit as st

st.title("Page Turners")

books = pd.read_csv("books.csv")

st.subheader("Preview of the book data")
st.dataframe(books.head())

st.subheader("Dataset size")
st.write("Number of rows:", books.shape[0])
st.write("Number of columns:", books.shape[1])

st.subheader("Missing values in each column")
st.dataframe(books.isna().sum())