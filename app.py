import streamlit as st
import pandas as pd
import joblib
from PIL import Image

model= open("model_uas.pkl", "rb")
ab_clf=joblib.load(model)


st.title("Aplikasi untuk mengklasifikasikan spesies pada bunga Iris")


setosa     = Image.open('setosa.png')
versicolor = Image.open('iris_versicolor.png')
virginica  = Image.open('virginica.png')

st.sidebar.title("Fitur-fitur")


parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']

values=[]


for parameter, parameter_df in zip(parameter_list, parameter_default_values):
    
    values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
    parameter_input_values.append(values)
 
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')


if st.button("Click Here to Classify"):
	prediction = ab_clf.predict(input_variables)
	st.image('setosa.png') if prediction == 0 else st.image('iris_versicolor.png') if prediction == 1 else st.image('virginica.png') 
	
