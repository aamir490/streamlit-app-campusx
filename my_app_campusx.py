# streamlit run my_app_campusx.py   <----------- RUN

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import time
import datetime

# Set the configuration for the Streamlit page
st.set_page_config(layout='wide', page_title='StartUp Analysis', initial_sidebar_state='expanded')

# Load the dataset using the provided file path
df = pd.read_csv('E:/cloud/python/python-lab/streamlit-basics/startup_cleaned.csv')

# Convert 'date' column to datetime if it exists
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')


# Define the function to load investor details
def load_investor_details(investor):
    st.title(investor)

    # Load the most recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor, na=False)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    # Display biggest investments
    col1, col2, col3 = st.columns(3)

    with col1:
        # Biggest investments
        big_series = df[df['investors'].str.contains(investor, na=False)].groupby('startup')[
            'amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        ax.set_xlabel('Startups')
        ax.set_ylabel('Amount (in USD)')
        ax.set_title('Top 5 Biggest Investments')
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor, na=False)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.1f%%", startangle=140)
        ax1.set_title('Investment Distribution by Sector')
        st.pyplot(fig1)

    with col3:
        city_series = df[df['investors'].str.contains(investor, na=False)].groupby('city')['amount'].sum()
        st.subheader('Investment by City')
        fig2, ax2 = plt.subplots()
        ax2.pie(city_series, labels=city_series.index, autopct="%0.1f%%", startangle=140)
        ax2.set_title('Investment Distribution by City')
        st.pyplot(fig2)

    print(df.info())

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)

    st.pyplot(fig2)


# Sidebar configuration
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
    # Uncomment the following line if you have the function to load overall analysis
    # load_overall_analysis()

elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    if btn1:
        st.title(f'StartUp Analysis: {selected_startup}')
        # Uncomment the following line if you have the function to load startup details
        # load_startup_details(selected_startup)

else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)



