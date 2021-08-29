import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly as px

from end_code_block import end_code_block as __


def app():
    st.title('Lesson #7 Activity Book for MBA509')
    st.markdown('----')
    st.header("Hi, this is our book of quizzes on algorithms and artificial intelligence")
    
    st.markdown('----')
    st.header("In machine learning, we often encounter variables X and y?")
    ai = st.radio(
    "Select that which is correct",
    ('X and y: X marks the spot and y is the vertical axis', 'X and y: X are the features and y is the vertical axis', 'X and y: X are the features and y is the target', 'X and y: X marks the spot and y is the dependent variable', 'X and y: X is the target and y are the features'))
    
    # definitions learning outcomes
    st.header("In machine learning, an epoch is?")
    algo = st.radio(
    "Select the correct answer",
    ('is an instant moment in time', 'a time period longer than an age but shorter than a period', 'a long period of time, with new developments and great change', 'one epoch is when an entire dataset is passed forward and backward through the neural network only once', 'one epoch is when an entire dataset is passed forward and backward through the neural network only over a long period of time'))
    
    st.header("Learning rate")
    learner = st.radio(
    "Select the correct answer",
    ('learning rate is how AI/ML climbs a hill', 'learning rate is how AI/ML descends into a valley', 'learning rate is sometimes called the step-size', 'learning rate is how AI/ML learns'))
    
    st.header("High learning rate")
    highrate = st.radio(
    "Select the correct answer",
    ('A high learning rate is good for AI/ML','A high learning rate is bad for AI/ML', 'Too high a learning rate and the learning process will be much more unstable', 'Low learning rates means that AI/ML learns really quickly'))
    
    st.header("Low learning rate")
    lowrate = st.radio(
    "Select the correct answer",
    ('A low learning rate is good for AI/ML','A low learning rate is bad for AI/ML', 'Too low a learning rate and the learning process takes much longer', 'Low learning rates means that AI/ML learns becomes unstable'))
    
    

    
    
    
    