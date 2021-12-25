from tensorflow import keras
from prediction import pred
import streamlit as st 
import numpy as np

model = keras.models.load_model('survival')



def main():
    st.header('Patient Survival Prediction')

    st.write('This is a simple demo of the Streamlit framework')
    st.write('It demonstrates how to load a model, make predictions, and display the results')
    st.write('The model was trained on the Patient Survival Dataset')

    st.subheader('Input the Data')
    st.write('Please input the data below')

    i = st.number_input('apache_4a_hospital_death_prob',)
    j = st.number_input('apache_4a_icu_death_prob',)
    k = st.number_input('age',)
    l = st.number_input('d1_spo2_min',)
    m = st.number_input('d1_resprate_max',)
    n = st.number_input('d1_heartrate_min',)


    input = np.array([[i,j,k,l,m,n]])
    print(type(i))
    print(input)
    
    
    if st.button("Find out patient's survival"):
        predi = pred(model,[i,j,k,l,m,n])
        st.success('The predicted is ' + 'alive' if predi==0 else 'dead')

     
if __name__ == '__main__':

    main()