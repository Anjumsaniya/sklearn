# -*- coding: utf-8 -*-
"""iris_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JMzxkTfoWn1gBfk13F4icg6aBYoJ4L9y
"""

import streamlit as st
import numpy as np
import joblib

st.markdown('## Iris Species Prediction')
sepal_length = st.number_input('sepal length (cm)')
sepal_width = st.number_input('sepal width (cm)')
petal_length = st.number_input('petal length (cm)')
petal_width = st.number_input('petal width (cm)')

if st.button('predict'):
    model = joblib.load('iris_model.pkl')
    X = np.array([sepal_length, sepal_width, petal_length, petal_width])
    if any(X <= 0):
      st.markdown('### inputs must be greater than 0')
    else:
      st.markdown('### Prediction is{model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]}')

streamlit==0.79.0
numpy==1.19.2
joblib==0.17.0
scikit-learn==0.23.2