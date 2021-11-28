import streamlit as st
import pandas as pd


file = st.file_uploader("Please upload an image file or...", type=["csv", "txt"])

df = pd.read_csv(file)

st.write(pd)