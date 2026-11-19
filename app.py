import pandas as pd
import streamlit as st

st.title("Page Turners")

books = pd.read_csv("books.csv")

st.subheader("Preview of the book data")
st.dataframe(books.head())
