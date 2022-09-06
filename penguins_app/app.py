import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Welcome to the first penguin dataset app")

st.write("**Starting** the *build* of penguin app :penguin: :mag:")

st.write("Data is taken from [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)")

st.header("DATA")

df= pd.read_csv("penguins_extra.csv")

st.write("Display a sample of 20 datapoints", df.sample(20))

species = st.selectbox(f"Select species", df.species.unique())

st.write(f"Displaying a subdata from {species}", df[df["species"]== species])

#Heading over to the plotting 

fig,ax = plt.subplots()
ax= sns.scatterplot(
    data=df,
    x="bill_length_mm", 
    y= "flipper_length_mm",
    hue="species"
    )

st.pyplot(fig)


st.bar_chart(df.groupby("island")["species"].count())

st.map(df)

csv_variable = st.sidebar.file_uploader("Upload a csv file", type = ["csv"])

if csv_variable is not None:
    df = pd.read_csv(csv_variable)
    st.write(df)