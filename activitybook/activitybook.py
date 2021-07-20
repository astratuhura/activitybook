import os
import streamlit as st
from PIL import  Image

# multiple pages handler 
from multipage import multi_page

# import apps from source (src) directory
from src import lesson_one_activities


# instantiate multipage app handler
app = multi_page()

# main title as app entry point
st.title('MBA509 AI Programming for Business Analytics')
st.title('Activity Book')
st.write('This Activity Book contains short quizes to test your knowledge of material that is covered is the weekly lessons.')

# left and right columns
left_col, right_col = st.beta_columns(2)

st.sidebar.header('Navigation to Activity Books')

# add apps
app.add_page("Lesson #1 Activities", lesson_one_activities.app)

# run main app
app.run()