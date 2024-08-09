# streamlit run basic_code.py
# Streamlit is an open-source Python library that allows you to quickly create and share web applications
#   for data science and machine learning projects.
# It’s designed to be simple and easy to use, letting you turn Python scripts into interactive web apps with just
#   a few lines of code.

# With Streamlit, you can build and deploy data dashboards, visualizations, and user interfaces
#    without needing to dive into HTML, CSS, or JavaScript.
# It’s particularly popular for prototyping machine learning models and data visualizations.

import streamlit as st
import pandas as pd

# Title of the app
st.title('Basic Streamlit App for Pandas')

# Read data from CSV
df = pd.read_csv('https://drive.google.com/file/d/1-Bbq2uz4RqIk1-lkUOVjf5tewsXbjLgV/view?usp=drive_link')

# Display the DataFrame
st.write('Here is the dataset:')
st.write(df)

# Add a slider to filter data by age
age_filter = st.slider('Filter by age:', min_value=int(df['age'].min()), max_value=int(df['age'].max()), value=int(df['age'].max()))

# Filter the DataFrame based on the slider value
filtered_df = df[df['age'] <= age_filter]

# Display the filtered DataFrame
st.write(f'Data for ages <= {age_filter}:')
st.write(filtered_df)
