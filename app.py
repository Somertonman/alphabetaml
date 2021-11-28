import streamlit as st
import pandas as pd


file = st.file_uploader("Please upload an image file or...", type=["csv", "txt"])

if file:
	df = pd.read_csv(file)
	st.write(df.head())


if file:
	ab_column = st.sidebar.selectbox("Test/control group selector", df.columns)
	resulting_parameter = st.sidebar.selectbox("Resulting column", df.columns)
	st.write(ab_column)
	simple_stat(ab_column, resulting_parameter)


def simple_stat(ab_column, resulting_parameter):
	ab_par = df.groupby(ab_column)[resulting_parameter].sum()/df.groupby(ab_column)[resulting_parameter].count()*100
	st.write(ab_par)