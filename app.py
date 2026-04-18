import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Yulu Bike Demand Prediction", layout="centered")

st.title("🚲 Yulu Bike Demand Prediction System")
st.write("Enter the details below to predict bike rental demand.")

# Inputs
season = st.selectbox("Season", [1, 2, 3, 4])
yr = st.selectbox("Year", [0, 1])
mnth = st.selectbox("Month", list(range(1, 13)))
hr = st.slider("Hour", 0, 23, 8)
holiday = st.selectbox("Holiday", [0, 1])
weekday = st.selectbox("Weekday", list(range(0, 7)))
workingday = st.selectbox("Working Day", [0, 1])
weathersit = st.selectbox("Weather Situation", [1, 2, 3, 4])
temp = st.slider("Temperature", 0.0, 1.0, 0.5)
atemp = st.slider("Feels Like Temperature", 0.0, 1.0, 0.5)
hum = st.slider("Humidity", 0.0, 1.0, 0.5)
windspeed = st.slider("Windspeed", 0.0, 1.0, 0.2)

# Derived features
day = 15
is_weekend = 1 if weekday in [0, 6] else 0
rush_hour = 1 if (7 <= hr <= 9 or 17 <= hr <= 20) else 0

input_df = pd.DataFrame([{
    "season": season,
    "yr": yr,
    "mnth": mnth,
    "hr": hr,
    "holiday": holiday,
    "weekday": weekday,
    "workingday": workingday,
    "weathersit": weathersit,
    "temp": temp,
    "atemp": atemp,
    "hum": hum,
    "windspeed": windspeed,
    "day": day,
    "is_weekend": is_weekend,
    "rush_hour": rush_hour
}])

# Prediction
if st.button("Predict Demand"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Bike Rentals: {int(prediction)}")

    if prediction < 100:
        st.info("Demand Level: Low")
    elif prediction < 300:
        st.warning("Demand Level: Medium")
    else:
        st.error("Demand Level: High")