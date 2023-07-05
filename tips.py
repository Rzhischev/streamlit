#Возьмите своё исследование по чаевым (датасет tips.csv) визуализируйте его на платформе Streamlit

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
st.write("""
# tips.csv data research
""")
# Общий сэтап
sns.set(rc={ 'ytick.color': 'grey', 'xtick.color': 'grey','axes.edgecolor': 'None', 'axes.axisbelow': 'line', 'figure.facecolor':'None', 'axes.facecolor': 'none', 'axes.grid': False, 'axes.labelcolor': 'white'})  
st.write(""" 
### 1 | Total bill histogram
""")
fig,ax = plt.subplots()
sns.histplot(tips, x='total_bill', bins=10, color='yellowgreen', fill=False)
plt.xlabel('Total bill')

st.pyplot(fig)


st.write("""
### 2 | Scatterplot (Total bill and Tip)
""")

fig, ax=plt.subplots()
sns.scatterplot(tips, x='total_bill', y='tip', c=None, linewidth=1)
plt.ylabel('Tips')
plt.xlabel('Total bill')
st.pyplot(fig) 

st.write("""
### 3 | Scatter Total, Tip and Size
""")

fig,ax=plt.subplots()
sns.scatterplot(tips, x='total_bill', y='tip', hue='size', color='green')
plt.ylabel('Tips')
plt.xlabel('Total bill')
st.pyplot(fig)



st.write("""
### 4 | Total by day
""")
fig = plt.figure() 
tips_by_day = tips.sort_values(by='total_bill').reset_index()
tips_by_day['day'] = pd.Categorical(tips_by_day['day'],
                            categories=['Thur', 'Fri', 'Sat', 'Sun'], ordered=True)
tips_by_sorted = tips_by_day.groupby('day')['total_bill'].mean()

      
sns.lineplot(tips_by_sorted, c='yellowgreen')
plt.ylabel('Total bill')
plt.xlabel('Days')
st.pyplot(fig)


st.write("""
### 5 | Scatter (Tips, Day, Sex)
""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='tip', y='day', hue='sex')
plt.ylabel('Days')
plt.xlabel('Tips')
st.pyplot(fig)


st.write("""
### 6 | Box plot Total by Time (Dinner/Lunch)

""")

fig,ax=plt.subplots()
sns.boxplot(tips, x='day', y='total_bill', hue='time')
plt.ylabel('Total bill')
plt.xlabel('Days')
st.pyplot(fig)

st.write("""
### 7 | Sex-Total-Tips (Smokers or non)
""")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
tips_sm = tips.sort_values(by='total_bill').reset_index().sort_values('day')
ax1 = sns.scatterplot(tips_sm[tips_sm['sex']=='Female'], ax=axes[0], x='total_bill',y='tip', hue='smoker', size='size')
ax1.xaxis.set_major_locator(MaxNLocator(nbins='auto'))
plt.ylabel('Tips')
plt.xlabel('Total bill')
ax1.set_title('Females')


ax2 = sns.scatterplot(tips_sm[tips_sm['sex']=='Male'], ax=axes[1], x='total_bill',y='tip', hue='smoker', size='size')
ax2.xaxis.set_major_locator(MaxNLocator(nbins='auto'))
ax2.set_title('Males')
plt.ylabel('Tips')
plt.xlabel('Total bill')

st.pyplot(fig)


st.write("""
### 8 | Tips count (Dinner and Lunch)
""")
df = pd.DataFrame(tips, columns=['tip', 'time'])
grouped = df.groupby('time')['tip'].sum()

fig = plt.figure(figsize=(5,5))       
sns.histplot(tips, x='time', hue='time', color='yellowgreen', fill=False)
plt.ylabel('Count')
plt.xlabel('Time')
st.pyplot(fig)
