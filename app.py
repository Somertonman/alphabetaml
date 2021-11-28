import streamlit as st
import pandas as pd
import seaborn as sns


file = st.file_uploader("Please upload an image file or...", type=["csv", "txt"])

def simple_stat(ab_column, resulting_parameter):
	ab_par = df.groupby(ab_column)[resulting_parameter].sum()/df.groupby(ab_column)[resulting_parameter].count()*100
	items = list(ab_par.items())
	st.write(items)


def bootstrap_parameter(ab_column, resulting_parameter, iterations):
	boot_1d = []
	for i in range(iterations):
	    boot_mean = df.sample(frac=1, replace=True).groupby(ab_column)[resulting_parameter].mean()
	    boot_1d.append(boot_mean)
	    
	boot_1d = pd.DataFrame(boot_1d)

	fig = sns.kdeplot(boot_1d_sns.version)
	st.pyplot(fig)




	
if file:
	df = pd.read_csv(file)
	st.write(df.head())


if file:
	ab_column = st.sidebar.selectbox("Test/control group selector", df.columns)
	resulting_parameter = st.sidebar.selectbox("Resulting column", df.columns)
	st.write(ab_column)
	simple_stat(ab_column, resulting_parameter)
	bootstrap_parameter(ab_column, resulting_parameter, 300)




