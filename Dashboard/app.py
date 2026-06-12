    
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("../Models/risk_model.pkl")
scaler = joblib.load("../Models/scaler.pkl")

st.title("Financial Risk Modelling Dashboard")

st.write("Predict Loan Default Risk")

person_age = st.number_input("Age", min_value=18, max_value=100)

person_income = st.number_input("Income")

person_emp_length = st.number_input("Employment Length")

loan_amnt = st.number_input("Loan Amount")

loan_int_rate = st.number_input("Interest Rate")

loan_percent_income = st.number_input(
    "Loan Percent Income",
    min_value=0.0,
    max_value=1.0
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length"
)

if st.button("Predict Risk"):

    sample = [[
        person_age,
        person_income,
        2,
        person_emp_length,
        4,
        3,
        loan_amnt,
        loan_int_rate,
        loan_percent_income,
        0,
        cb_person_cred_hist_length
    ]]

    sample = scaler.transform(sample)

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("High Risk Customer")
    else:
        st.success("Low Risk Customer")