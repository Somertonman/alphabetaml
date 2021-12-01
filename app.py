import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


 
file_selection = st.radio("Please choose csv file OR use demo file", ('demo','file'))
if file_selection == 'file':
	file = st.file_uploader("Please upload an image file or...", type=["csv", "txt"])
elif file_selection == 'demo':
	st.write('cookie_cats.txt')
	st.write('Test/control group column - version and metric - retention_1 or retention_7 and press RUN')
	file = open('cookie_cats.txt', 'r')

def simple_stat(ab_column, resulting_parameter):
	ab_par = df.groupby(ab_column)[resulting_parameter].sum()/df.groupby(ab_column)[resulting_parameter].count()*100
	items = list(ab_par.items())
	st.write(items)


def bootstrap_parameter(ab_column, resulting_parameter, iterations):
	boot = []
	for i in range(iterations):
	    boot_mean = df.sample(frac=1, replace=True).groupby(ab_column)[resulting_parameter].mean()
	    boot.append(boot_mean)
	    
	boot = pd.DataFrame(boot)

	fig = plt.figure(figsize=(10, 4))
	sns.set_style("darkgrid", {"axes.facecolor": ".9"})
	sns.set_context("notebook")
	sns.kdeplot(data=boot)
	st.pyplot(fig)


def run_calc():
	simple_stat(ab_column, resulting_parameter)
	bootstrap_parameter(ab_column, resulting_parameter, 300)



	
if file:
	df = pd.read_csv(file)
	st.write(df.head())


if file:
	ab_column = st.sidebar.selectbox("Test/control group selector", df.columns)
	resulting_parameter = st.sidebar.selectbox("Resulting column", df.columns)
	if st.sidebar.button('Run'):
		run_calc()
	
	




