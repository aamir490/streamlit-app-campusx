#  TO RUN THIS FILE :---->>>  streamlit run Text_Utility2.py

# ----------- FOR IMPORT LIBRARAY -------------------------
# IMPORT LIBRARY :-
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
import datetime

#---------------------------------Button Example ----------------------------------------------
#-------------------------------------------------------------------------------
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
import datetime

# -------------------------------------------------
# Title of the app
st.title("Streamlit User Input and Image Upload Example")

# -------------------------------------------------
# User Input Section
st.header("User Authentication")
name = st.text_input('Enter your name:')
email = st.text_input('Enter your email:')
password = st.text_input('Enter password:', type='password')  # Secure text input
gender = st.selectbox('Select your gender', ['Male', 'Female', 'Others'])

# Button to trigger login
btn = st.button('Login')

# -------------------------------------------------
# Button Click Handling
if btn:
    # Simulate a loading process
    with st.spinner('Checking credentials...'):
        time.sleep(2)  # Simulate a delay for processing

    # Check credentials
    if email == 'cr7@gmail.com' and password == 'cr123':
        st.balloons()  # Show balloons on successful login
        st.success('Login Successful!')
        st.write(f'Welcome, {name}!')

        # Display current date
        today = datetime.date.today()
        st.write(f'Today\'s date is: {today}')

        # Display sample DataFrame
        df = pd.DataFrame({
            'Column 1': np.random.randn(5),
            'Column 2': np.random.randn(5)
        })
        st.write('Here is a sample DataFrame:')
        st.dataframe(df)

        # Display a simple plot
        st.write('Here is a sample plot:')
        fig, ax = plt.subplots()
        ax.plot(df['Column 1'], df['Column 2'], 'o-')
        st.pyplot(fig)

        # JSON Example
        json_data = {
            'user_name': name,
            'user': email,
            'status': 'Logged in',
            'gender': gender,
            'country': 'Portugal',
            'current_team': 'Al-Nassar'
        }
        st.write('### User Data in JSON format:')
        st.json(json_data)

    else:
        st.error('Login Failed! Please check your credentials.')

# -------------------------------------------------
# Image Upload Section
st.header("Image Upload Example")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # To read file as bytes:
    file_bytes = uploaded_file.read()
    st.image(file_bytes, caption='Uploaded Image', use_column_width=True)
    st.success('Image successfully uploaded!')
else:
    st.warning('No image uploaded yet.')


# Subheader :-
st.subheader('upload your data:-')

# Direct download link for the CSV file
csv_url = 'https://drive.google.com/file/d/19RkLdzmXimOir4atgAdJv2LYMJVG7mKV/view?usp=sharing'

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
# -------------------------------------------------

# Progress Bar Example
st.header("Progress Bar Example")
progress_bar = st.progress(0)

# Simulate a long-running task
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.05)

st.write('Progress Complete!')
# Success message
st.success('Profile Upload successfully!')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# Direct download link for the CSV file
csv_url = 'https://drive.google.com/file/d/19RkLdzmXimOir4atgAdJv2LYMJVG7mKV/view?usp=sharing'

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
# email = st.text_input('Enter email')
# password = st.text_input('Enter password')
# gender = st.selectbox('Select gender',['male','female','others'])
#
# btn = st.button('Login Karo')
#
# # if the button is clicked
# if btn:
#     if email == 'nitish@gmail.com' and password == '1234':
#         st.balloons()
#         st.write(gender)
#     else:
#         st.error('Login Failed')
#
#
#
# file = st.file_uploader('Upload a csv file')
#
# if file is not None:
#     df = pd.read_csv(file)
#     st.dataframe(df.describe())