import streamlit as st
import pandas as pd
import os

st.title("Patient Intake System")

bmi = None  # Ensure BMI exists globally

# --- Form for patient data ---
with st.form("intake_form"):
    st.subheader("New Patient Entry")
    
    # 1. Demographics
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    
    # 2. Clinical Data
    blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    is_smoker = st.checkbox("History of Smoking?")
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=1000.0)
    height = st.number_input("Height (cm)", min_value=0.0, max_value=300.0)
    
    # 3. Submit button (single action)
    submitted = st.form_submit_button("Submit Patient Data")

# --- After form submission ---
if submitted:
    # Calculate BMI automatically
    if height > 0:
        bmi = round(weight / ((height / 100) ** 2), 2)
    else:
        st.error("Height must be greater than 0 to calculate BMI.")
        bmi = None

    # Create dictionary with all patient data + BMI
    new_data = {
        "Name": name,
        "Age": age,
        "Blood Type": blood_type,
        "Smoker": is_smoker,
        "Weight": weight,
        "Height": height,
        "BMI": bmi
    }

    # Convert to DataFrame
    df = pd.DataFrame([new_data])

    # Save to CSV
    file_path = "patient_database.csv"
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

    # Success message with BMI
    st.success(f"Patient {name} added successfully! BMI = {bmi}")

    # Obesity warning if BMI > 30
    if bmi is not None and bmi > 30:
        st.warning("Patient is in the Obesity range")
    if bmi is not None and bmi > 30:
        st.warning("Patient is in the Obesity range")
