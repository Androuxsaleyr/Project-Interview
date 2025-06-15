import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model_clean.pkl", "rb") as f:
    model = pickle.load(f)

st.markdown("<h1 style='color:#2E86C1;'>Telco Churn Prediction</h1>", unsafe_allow_html=True)

# Inputs that match encoded columns
city = st.selectbox("City", ['Houston', 'Los Angeles', 'Miami', 'New York', 'Chicago'])
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Married", ['Yes', 'No'])
offer = st.selectbox("Offer", ['None', 'Offer A', 'Offer B'])
phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No'])
internet_service = st.selectbox("Internet Service", ['Yes', 'No'])
internet_type = st.selectbox("Internet Type", ['DSL', 'Fiber Optic', 'Cable'])
online_security = st.selectbox("Online Security", ['Yes', 'No'])
online_backup = st.selectbox("Online Backup", ['Yes', 'No'])
device_protection = st.selectbox("Device Protection Plan", ['Yes', 'No'])
tech_support = st.selectbox("Premium Tech Support", ['Yes', 'No'])
streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No'])
streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No'])
streaming_music = st.selectbox("Streaming Music", ['Yes', 'No'])
unlimited_data = st.selectbox("Unlimited Data", ['Yes', 'No'])
contract = st.selectbox("Contract", ['Month-to-Month', 'One Year', 'Two Year'])
paperless = st.selectbox("Paperless Billing", ['Yes', 'No'])
payment_method = st.selectbox("Payment Method", ['Bank', 'Credit Card', 'Mailed Check'])
status = st.selectbox("Customer Status", ['Active', 'Inactive'])
age_cat = st.selectbox("Age Category", ['18-29', '30-49', '50-64', '65+'])

# Dummy encoded mappings (you must match these with actual LabelEncoder mappings used)
encode = lambda val: hash(val) % 10  # simple consistent mapping for demo

input_data = pd.DataFrame([{
    'City_encoded': encode(city),
    'Gender_encoded': 1 if gender == 'Male' else 0,
    'Married_encoded': 1 if married == 'Yes' else 0,
    'Offer_encoded': encode(offer),
    'Phone_Service_encoded': 1 if phone_service == 'Yes' else 0,
    'Multiple_Lines_encoded': 1 if multiple_lines == 'Yes' else 0,
    'Internet_Service_encoded': 1 if internet_service == 'Yes' else 0,
    'Internet_Type_encoded': encode(internet_type),
    'Online_Security_encoded': 1 if online_security == 'Yes' else 0,
    'Online_Backup_encoded': 1 if online_backup == 'Yes' else 0,
    'Device_Protection_Plan_encoded': 1 if device_protection == 'Yes' else 0,
    'Premium_Tech_Support_encoded': 1 if tech_support == 'Yes' else 0,
    'Streaming_TV_encoded': 1 if streaming_tv == 'Yes' else 0,
    'Streaming_Movies_encoded': 1 if streaming_movies == 'Yes' else 0,
    'Streaming_Music_encoded': 1 if streaming_music == 'Yes' else 0,
    'Unlimited_Data_encoded': 1 if unlimited_data == 'Yes' else 0,
    'Contract_encoded': encode(contract),
    'Paperless_Billing_encoded': 1 if paperless == 'Yes' else 0,
    'Payment_Method_encoded': encode(payment_method),
    'Customer_Status_encoded': encode(status),
    'Age_Categories_encoded': encode(age_cat)
}])

# Predict button
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Churn: {'Yes' if prediction == 1 else 'No'}")
