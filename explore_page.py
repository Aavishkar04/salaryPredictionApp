import streamlit as st
import pandas as pd
import altair as alt

# Function to load data
@st.cache_data
# or
# @st.cache_resource
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "ConvertedComp"]]
    df = df.dropna()
    df = df[df["ConvertedComp"] > 10000]  # Filter out salaries below $10,000
    return df

df = load_data()

base="dark"
primaryColor="purple"

# Function to show explore page
def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write("### Stack Overflow Developer Survey 2020")

    st.write("#### Distribution of Salaries")
    hist = alt.Chart(df).mark_bar().encode(
        alt.X("ConvertedComp:Q", bin=alt.Bin(maxbins=30), title="Salary (USD)"),
        alt.Y("count()", title="Number of Respondents"),
        tooltip=[alt.Tooltip("ConvertedComp:Q", bin=alt.Bin(maxbins=30), title="Salary (USD)"), "count()"]
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(hist)

    st.write("#### Mean Salary Based On Country")
    data_country = df.groupby(["Country"])["ConvertedComp"].mean().reset_index()
    chart_country = alt.Chart(data_country).mark_bar().encode(
        x='Country',
        y='ConvertedComp',
        tooltip=['Country', 'ConvertedComp']
    ).properties(
        width=600,
        height=400
    ).interactive()
    st.altair_chart(chart_country)

# Call the function to show the Explore page
show_explore_page()
