import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly as px

from end_code_block import end_code_block as __


def app():
    st.title('Lesson #5 Activity Book for MBA509')
    st.markdown('----')
    st.header("Hi, this is our book of quizzes on algorithms and artificial intelligence")
    st.markdown('----')
    
    # definitions learning outcomes
    st.write("Handling missing data")
    st.write("Python and Pandas have many ways to handle missing data. Which one of these is a method provided by Pandas?")
    algo = st.multiselect(
    "Select all that applies",
    ('fill_it()', 'fill_many()', 'fill_more()', 'fillna()', 'fill_none()'))

    st.write("What are Data attributes?")
    data_attributes = st.multiselect(
    'Data Attributes:',
    ['All columns of data', 'Some columns of data', 'Data that do not influence the outcomes of a prediction or a forecasting problem', 'Are structured data', 'Are unstructured data'],
    ['All columns of data', 'Some columns of data', 'Data that do not influence the outcomes of a prediction or a forecasting problem', 'Are structured data', 'Are unstructured data'])

    st.write('You selected:', data_attributes)

    st.markdown('----')
    st.write("What is Pandas?")
    ai = st.radio(
    "Pandas is:",
    ('A cute bear', 'A data analytics library'))

    st.markdown('----')
    st.write("What are variables?")
    ai = st.radio(
    "Variables are:",
    ('A number', 'A name', 'A name we design to store data'))

    st.markdown('----')
    st.write("The following statement uses Pandas read CSV data correctly:")
    ai = st.radio(
    "Select the correct statement",
    ('pd.load_csv('')', 'pd.read_csv('')', 'pd.import_csv('')', 'pd.upload_csv('')'))

    st.markdown('----')
    st.header("What is the difference between forecasting and prediction?")
    st.write("Forecasting is?")
    ai = st.radio(
    "Select the correct definition",
    ('estimate future trends', 'predicts the future', 'estimates future trends with  time series data'))

    st.markdown('----')
    st.header("What is an artificial neural network?")
    st.write("Select that which is most correct")
    ai = st.radio(
    "Select the correct definition",
    ('simulates the behaviour of the human brain, and this simulation allows ANNs to recognise patterns in data and solve business problems', 'simulates the behaviour of the human brain, to recognise patterns in data and predict the future', 'simulates the behaviour of the human brain, makes forecasts'))
    
    st.markdown('----')
    st.header("What are the two basic types of primitives?")
    st.write("Select that which is most correct")
    ai = st.radio(
    "Select the correct definition",
    ('Aggregation and transformation', 'Multiplication and Addition', 'Mutliplication and subtraction', 'Transformation and addition', 'Aggregation and subraction'))
    
    st.markdown('----')
    st.header("Sometimes we encounter Python code that contains 'df'.")
    st.write("What is df?")
    ai = st.radio(
    "Select that which is correct",
    ('df stands for: do not filter', 'df stands for: do filter', 'df stands for: display floats', 'df stands for dataframe', 'df stands for: deep forest'))
    
    st.markdown('----')
    st.header("How do we obtain the name of the column in a dataframe?")
    st.write("Select the correct way.")
    ai = st.radio(
    "Select that which is correct",
    ('df.my_column', 'df.this_column', 'df.get_column', 'df.column_name', 'df.rows'))
    
    
    st.markdown('----')
    st.header("In machine learning, we often encounter variables X and y?")
    st.write("Select that which is correct.")
    ai = st.radio(
    "Select that which is correct",
    ('X and y: X marks the spot and y is the vertical axis', 'X and y: X are the features and y is the vertical axis', 'X and y: X are the features and y is the target', 'X and y: X marks the spot and y is the dependent variable', 'X and y: X is the target and y are the features'))