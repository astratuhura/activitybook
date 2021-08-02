import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly as px

from end_code_block import end_code_block as __


def app():
    st.title('Lesson #3 Activity Book for MBA509')
    st.markdown('----')
    st.header("Hi, this is our book of quizzes on algorithms and artificial intelligence")
    st.markdown('----')
    
    # definitions learning outcomes
    st.header("Different Types of Data")
    st.write("What kind of data do you see in the Airbnb Melbourne Listings?")
    algo = st.multiselect(
    "Select all that applies",
    ('Categorical', 'Continuous, Decimal', 'Discrete', 'Strings', 'Floats', 'Int', 'Boolean', 'Unstructured'))

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
    ('pd.load_csv('')', 'pd.read_csv('')', 'pd.import_csv('')'))

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
    st.header("What are primitives?")
    st.write("Select that which is most correct")
    reinforce_learn = st.multiselect(
    'Which of the following is a correct statement?',
    ['the fundamental building blocks of individual calculations applied to raw data', 'The agent receives a reward for reaching the goals', 'Agent learns by trial and error', 'Artificial Neural Networks (ANNs)','Random Forest Algorithms'],
    ['the fundamental building blocks of individual calculations applied to raw data', 'Agent learns by trial and error','Random Forest Algorithms'])
    st.markdown('----')
    
    st.markdown('----')
    st.header("What are the two basic types of primitives?")
    st.write("Select that which is most correct")
    ai = st.radio(
    "Select the correct definition",
    ('Aggregation and transformation', 'Multiplication and Addition', 'Mutliplication and subtraction', 'Transformation and addition', 'Aggregation and subraction'))