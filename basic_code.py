# streamlit run basic_code.py

import streamlit as st
import pandas as pd

# Title of the app
st.title('Basic Streamlit App for Pandas')

# Direct download link for the CSV file
csv_url = 'https://drive.google.com/uc?id=1-Bbq2uz4RqIk1-lkUOVjf5tewsXbjLgV&export=download'

# Read data from CSV
try:
    # Attempt to read with error handling
    df = pd.read_csv(
        csv_url,
        delimiter=',',  # Change if necessary (e.g., use '\t' for tab-delimited files)
        encoding='utf-8',  # Change encoding if necessary
        on_bad_lines='skip'  # Skip lines with too many fields
    )
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
except pd.errors.ParserError as e:
    st.error(f"Error parsing CSV file: {e}")
except Exception as e:
    st.error(f"Error loading CSV file: {e}")



