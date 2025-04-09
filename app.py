import pandas as pd
import pandas_datareader as pdr
import matplotlib.pylab as plt
plt.style.use('ggplot')
pd.options.display.max_rows = 200
import datetime
import streamlit as st

st.header("Open Positions and Unemployed Americans")
st.write("Maintained by Nick Winnenberg: Nick@Winnenberg.Org.")

#Pull Data
start = datetime.datetime (2000, 5, 1)
end = datetime.datetime (2025, 6, 1)
unemploy_pop_df = pdr.DataReader('UNEMPLOY', 'fred', start, end) #Unemployed Level - Monthly
open_positions_df = pdr.DataReader('JTSJOL', 'fred', start, end) #Open Positions - Monthly

unemploy_pop_df=unemploy_pop_df.reset_index()
open_positions_df=open_positions_df.reset_index()

staffing_level_df = pd.merge(unemploy_pop_df,open_positions_df,on="DATE",how="outer")

staffing_level_df = staffing_level_df.rename(columns={"UNEMPLOY":"Unemployed Americans","JTSJOL":"Open Positions","DATE":"Month"})

staffing_level_df.plot(x="Month", y=["Unemployed Americans","Open Positions"],ylabel="Americans")

st.line_chart(staffing_level_df,x="Month",y=["Open Positions","Unemployed Americans"],y_label="Americans (Thousands)")

st.header("Staffing Ratio")
st.write("How many jobs are available per unemployed American")
staffing_ratio_df=staffing_level_df
staffing_ratio_df["Staffing Ratio"] = staffing_ratio_df["Open Positions"]/staffing_ratio_df["Unemployed Americans"]
st.line_chart(staffing_ratio_df,x="Month",y="Staffing Ratio")