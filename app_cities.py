import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('world cities')
df = pd.read_csv('worldcities.csv')


fig, ax = plt.subplots(figsize=(20, 5))
df.groupby('country')['population'].sum().plot.bar(ax=ax)
st.pyplot(fig)

pop_slider = st.slider('Choose Population', 0, 40, 3.6) #st.sidebar.silder()
df = df[df.population >= pop_slider]

# create a multi select  capital_filter is a list
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults

# filter by capital
df = df[df.capital.isin(capital_filter)]

#show on the map
st.map(df)
#show df
st.write(df)