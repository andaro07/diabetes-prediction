import streamlit as st
import pandas as pd
import pickle

def load_data():
    with open("diabetes_model.pkl", "rb") as file:
        data = pickle.load(file)
        return data

data = load_data()

model = data['model']
le_gender = data["le_gender"]

def show_page():
    st.title(":blue[MACHINE LEARNING MODEL PREDICTION OF DIABETES STATUS]")
    st.subheader("BY: ANIM RONALD DARKO")
    gender = st.selectbox(":blue[Gender]", ("Male", "Female", "Other"))
    h_disease = st.selectbox(":blue[Heart Disease History]", (0,1))
    hBac = st.slider(":blue[Glycated Haemoglobin Level]", 3.5, 9.0, 5.0)
    bmi = st.slider(":blue[Body Mass Index (BMI)]", 10, 96, 45)
    age = st.slider(":blue[Age]", 0, 80, 40)
    hyper = st.selectbox(":blue[Hypertension History]", (0,1))
    btn = st.button(":rainbow[Predict]")

    if btn:
        predictors = pd.DataFrame({
        "gender":[gender],
        "heart_disease": [h_disease],
        "HbA1c_level": [hBac],
        "bmi": [bmi],
        "age": [age],
        "hypertension":[hyper]
        })

        predictors.gender = le_gender.transform(predictors.gender)

        # st.dataframe(predictors)

        result = model.predict(predictors)

        st.write(f"The individual might {':red[have]' if result==1 else ':green[not have]'} Diabetes.")