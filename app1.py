import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model_uas.pkl", "rb") as f:
    model = pickle.load(f)

# Load images
image_dict = {
    "setosa": "setosa.png",
    "versicolor": "iris_versicolor.png",
    "virginica": "virginica.png"
}

# UI
st.write("""
# Iris Flower Prediction App
This app predicts the species of an Iris flower based on its sepal length, sepal width, petal length, and petal width.
""")

# User input
sepal_length = st.text_input("Sepal length", "5.4")
sepal_width = st.text_input("Sepal width", "3.4")
petal_length = st.text_input("Petal length", "1.3")
petal_width = st.text_input("Petal width", "0.2")

# Prediction
if st.button("Predict"):
    result = model.predict([[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]])
    species = result[0]
    st.write("The species of this flower is:", species)
    st.image(image_dict[species], width=200)