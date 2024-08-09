# TO RUN THIS CODE --> go to terminal --> streamlit run first_streamlit_code.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as

# Title of the app
st.title('Simple Streamlit App')

# Slider for user input
slider_value = st.slider('Select a number', 1, 100, 25)

# Generate some data based on slider value
data = pd.DataFrame({
    'x': np.arange(1, slider_value + 1),
    'y': np.random.randint(1, 100, slider_value)
})

# Display the data in a table
st.write('Data:')
st.write(data)

# Plotting the data
st.write('Line Chart:')
st.line_chart(data.set_index('x'))
