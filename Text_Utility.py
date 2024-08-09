
#  TO RUN THIS FILE :---->>>  streamlit run Text_Utility.py

# ----------- FOR IMPORT LIBRARAY -------------------------
# IMPORT LIBRARY :-
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
import datetime
# -------------------------------------------------

# ----------- FOR HEADING -------------------------
# Title of the app. (Main heading Big in size)
st.title('This is Main heading (HEADING 1)')

# Header ( below The main heading)
st.header('below The main heading (HEADING 2)')

# Subheader ( below the header)
st.subheader('below the header (HEADING 3)')
# -------------------------------------------------


# -------------- # FOR FORMATED TEXT ----------------
# # Markdown (useful for formatted text)
st.title('useful for formatted tex:-----')
st.markdown('**This is bold text**')
st.markdown('_This is italic text_')
st.markdown('**_This is bold and italic text_**')
st.markdown(""""
### MY ALL TIME FVT FOOTBALLERS:-
 - cR7  (Ronaldo)
 - lM10 (Messi)
 - nJ17 (Neymar)
""")
# -------------------------------------------------

# -------------- # FOR NORMAL TEXT-----------------
# # Text (plain text)
st.title('for plain text:-----')
st.text('This is plain & normal text.')
# -------------------------------------------------

# -------------- # FOR VARIOUS DATA TYPES & OTHERS ----------------------------------------------------------------
# # Write function (can handle various data types including text)
st.title('Write function (can handle various data types including text:-----')
st.write('This is a line of text written using `st.write`. It can also display data like DataFrames, charts, etc.')
# -----------------------------------------------------------------------------------------------------------------

# -------------- # Code (formatted text for code snippets) -----
# # Code (formatted text for code snippets)
st.title('Code (formatted text for code snippets:-----')
st.text('Basic code in st,code')
st.code('''
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to add two numbers
def add_two_numbers(a, b):
    return a + b

# Example usage
num1 = 5
num2 = 3

result = add_two_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
''', language='python') #  Enables syntax highlighting for Python code within the st.code function.

# -------------------------------------------------

# -------FOR MATHEMATICALL EXPRESSION ----------
st.title('FOR MATHEMATICALL EXPRESSION:-----')
st.text('Streamlit with LaTeX')

# Using st.latex for more control
st.latex(r'''
\frac{1}{1 + e^{-x}}
''')
# -----------------------------------------------


# ------------------- FOR MESSAGES ----------------------
st.title('FOR MESSAGES:-----')
# Success message
st.success('This is a success message!')

# Information message
st.info('This is an informational message.')

# Warning message
st.warning('This is a warning message.')

# Error message
st.error('This is an error message.')
# -------------------------------------------------------
#######################################################################################
#######################################################################################

## display ---> DataFrame, metrics ,json

# -------------------------------------------------------
# Title of the app
st.title('Streamlit DataFrame Example with st.dataframe')

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [23, 25, 22, 24, 23],
    'Score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

# Display the DataFrame interactively
st.write('### Interactive DataFrame:')
st.dataframe(df)
# -------------------------------------------------------



# --------------------- metrics ----------------------------------
# Calculate some metrics
average_age = df['Age'].mean()
average_score = df['Score'].mean()
total_entries = len(df)

# Display metrics
st.write('### Metrics:')
st.metric(label='Average Age', value=f'{average_age:.2f}')
st.metric(label='Average Score', value=f'{average_score:.2f}')
st.metric(label='Total Entries', value=str(total_entries))
# -------------------------------------------------------



# --------------------- # json----------------------------------
# Sample JSON data
# Title of the app
st.title('Streamlit JSON Example with st.json')

# Sample JSON data
json_data = {
    'user': 'Cristinao',
    'age': 39,
    'goals': 900,
    'details': {
        'location': 'Portugal',
        'status': 'Active'
    },
    'teams': ['RM', 'Mu', 'AlNasaar']
}

# Display the JSON data
st.write('### JSON Data:')
st.json(json_data)
# -------------------------------------------------------



# ------------------------# image -------------------------------
import streamlit as st

# Title of the app
st.title('Streamlit Image Example')

# Path to the image file
image_path = 'crpic.jpg'

# Display the image
st.image(image_path, caption='CRISTANO RONALDO Image', use_column_width=True)
# -------------------------------------------------------


# -------------------------------------------------------
import streamlit as st

# Title of the app
st.title('Simple Streamlit App with Sidebar and Columns')

# Sidebar
st.sidebar.header('Sidebar')
option = st.sidebar.selectbox('Choose an option:', ['Home', 'About'])

# Main content based on the selected option
if option == 'Home':
    st.write('You selected the Home option.')
    st.write('This is the main content area.')
elif option == 'About':
    st.write('You selected the About option.')
    st.write('This is the About section.')

# Columns
st.write('### Columns Example:')
col1, col2 = st.columns(2)

with col1:
    st.write('This is the first pic.')
    st.image("crpic.jpg")

with col2:
    st.write('This is the second pic.')
    st.image("crpic2.jpg")

# -------------------------------------------------------


# -------------# progress bar------------------------------------------
# import time
#
# # Title of the app
# st.title('Streamlit Progress Bar Example')
#
# # Create a progress bar
# progress_bar = st.progress(0)
#
# # Start a loop to simulate a long-running task
# for i in range(100):
#     # Update the progress bar
#     progress_bar.progress(i + 1)
#     # Simulate some work with sleep
#     time.sleep(0.1)
#
# st.write('Task Completeeeeee!')
# -------------------------------------------------------


# -------------------# user INPUT ------------------------------------
import datetime

# Title of the app
st.title('Streamlit User Input Example')

# Text Input
name = st.text_input('Enter your name:--')

# Number Input
age = st.number_input('Enter your age:', min_value=0, max_value=120, step=1)

# Slider
score = st.slider('Select your score:', min_value=0, max_value=100, value=50)

# Date_Input
dob = st.date_input('Select your date of birth:', min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())


# Button
if st.button('Submit'):
    st.write(f'Hello, {name}!')
    st.write(f'You are {age} years old.')
    st.write(f'Your score is {score}.')
    st.write(f'You selected: {dob}')

# -------------------------------------------------------



# -------------------------------------------------------

# -------------------------------------------------------



