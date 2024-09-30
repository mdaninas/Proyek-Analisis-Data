import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Streamlit titles and subtitles
st.title('Stasiun Bus Dengan Curah Hujan Tinggi dan Temperatur Tinggi')
st.subheader('Stasiun Dengan Curah Hujan Tinggi')

# List of stations with high rain
my_rain = ['Stasiun Wanliu', 'Stasiun Guanyuan', 'Stasiun Aotizhongxin']
for item in my_rain:
    st.markdown(f"- {item}")

# Read the CSV files
hujan_df = pd.read_csv("./dashboard/dataset1.csv")
panas_df = pd.read_csv("./dashboard/dataset2.csv")

# Create a rain bar plot
plt.figure(figsize=(12, 8))
sns.barplot(
    y='station', 
    x='RAIN', 
    data=hujan_df, 
    palette='Blues_d', 
    ci=None  
)
plt.title("Stasiun Dengan Curah Hujan Tertinggi", fontsize=16)
plt.xlabel("Curah Hujan", fontsize=14)
plt.ylabel("Stasiun", fontsize=14)

# Display the plot in Streamlit
st.pyplot(plt)

# Subtitle for stations with high temperatures
st.subheader('Stasiun Dengan Temperature Tinggi')
my_hot = ['Stasiun Gucheng', 'Stasiun Dingling', 'Stasiun Changping']
for item in my_hot:
    st.markdown(f"- {item}")

# Create a temperature bar plot
plt.figure(figsize=(12, 8))
sns.barplot(
    y='station', 
    x='TEMP', 
    data=panas_df,  # Use panas_df for temperature data
    palette='Reds_d', 
    ci=None  
)
plt.title("Stasiun Dengan Temperature Terpanas", fontsize=16)
plt.xlabel("Temperature", fontsize=14)
plt.ylabel("Stasiun", fontsize=14)

# Display the second plot in Streamlit
st.pyplot(plt)
