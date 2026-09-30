import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("landslide_model.pkl")

# Page settings
st.set_page_config(
    page_title="Landslide Risk Monitor",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Landslide Risk Monitor")
st.write("Enter environmental conditions to estimate landslide risk.")

# Input values
rainfall = st.number_input(
    "🌧️ Rainfall",
    min_value=0.0,
    value=50.0
)

soil_moisture = st.number_input(
    "💧 Soil Moisture",
    min_value=0.0,
    value=50.0
)

temperature = st.number_input(
    "🌡️ Temperature",
    value=25.0
)

humidity = st.number_input(
    "💦 Humidity",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

soil_tilt = st.number_input(
    "📐 Soil Tilt",
    value=5.0
)

# Prediction
if st.button("🔍 Check Landslide Risk"):

    input_data = pd.DataFrame([{
        "rainfall": rainfall,
        "soil_moisture": soil_moisture,
        "temperature": temperature,
        "humidity": humidity,
        "soil_tilt": soil_tilt
    }])

    prediction = model.predict(input_data)[0]

    # Display result
    if str(prediction).upper() == "LOW":
        st.success("🟢 Landslide Risk: LOW")
        st.info("Current input conditions indicate a relatively low predicted risk.")

    elif str(prediction).upper() == "MEDIUM":
        st.warning("🟡 Landslide Risk: MEDIUM")
        st.info("Monitor environmental conditions and changes in rainfall or soil moisture.")

    elif str(prediction).upper() == "HIGH":
        st.error("🔴 Landslide Risk: HIGH")
        st.warning("The model predicts elevated landslide risk. Environmental conditions should be monitored carefully.")

    else:
        st.subheader(f"🌋 Landslide Risk: {prediction}")