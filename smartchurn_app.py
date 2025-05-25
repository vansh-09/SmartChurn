import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
model = pickle.load(open('smartchurn_model.pkl', 'rb'))


st.title("📉 SmartChurn – Customer Churn Predictor")
st.markdown("Predict whether a telecom customer is likely to churn.")

# User Inputs
st.subheader("Customer Details")
tenure = st.slider("Tenure (months)", 0, 72, key="tenure")
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, key="monthly")
total_charges = st.number_input("Total Charges", min_value=0.0, key="total")

contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'], key="contract")
internet = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'], key="internet")
security = st.selectbox("Online Security", ['No', 'Yes'], key="security")
tech_support = st.selectbox("Tech Support", ['No', 'Yes'], key="tech")
payment = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key="payment")


def preprocess_inputs(tenure, monthly_charges, total_charges, contract, internet, security, tech_support, payment):
    input_data = {
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],

        'Contract_One year': [1 if contract == 'One year' else 0],
        'Contract_Two year': [1 if contract == 'Two year' else 0],

        'InternetService_Fiber optic': [1 if internet == 'Fiber optic' else 0],
        'OnlineSecurity_Yes': [1 if security == 'Yes' else 0],
        'TechSupport_Yes': [1 if tech_support == 'Yes' else 0],

        'PaymentMethod_Electronic check': [1 if payment == 'Electronic check' else 0],
    }

    # Add missing features with 0
    for col in model.feature_names_in_:
        if col not in input_data:
            input_data[col] = [0]

    return pd.DataFrame(input_data)[model.feature_names_in_]

# Prediction Trigger
if st.button("Predict"):
    input_df = preprocess_inputs(tenure, monthly_charges, total_charges, contract, internet, security, tech_support, payment)
    prediction = model.predict(input_df)[0]
    st.subheader("Prediction Result:")
    st.success("✅ Customer is **likely to stay**" if prediction == 0 else "⚠️ Customer is **likely to churn**")