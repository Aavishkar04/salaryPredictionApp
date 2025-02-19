import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Sidebar menu
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ("Predict Salary", "Explore Salaries"))

# Page selection
if page == "Predict Salary":
    show_predict_page()
else:
    show_explore_page()
