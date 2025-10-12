import streamlit as st
import numpy as np
import pickle

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

# Streamlit page config
st.set_page_config(page_title="California Housing Price Prediction", page_icon="🏠", layout="centered")

# Title
st.title("🏠 California Housing Price Prediction App")
st.markdown("Predict house prices based on key housing and demographic features.")

# Sidebar input section
st.sidebar.header("Input Features")

# Input sliders and dropdowns for only important features
longitude = st.sidebar.slider("Longitude", -125.0, -114.0, -120.0)
latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 36.5)
housing_median_age = st.sidebar.slider("Housing Median Age", 1, 52, 20)
total_rooms = st.sidebar.slider("Total Rooms", 100, 40000, 2000)
total_bedrooms = st.sidebar.slider("Total Bedrooms", 50, 5000, 400)
population = st.sidebar.slider("Population", 100, 50000, 1000)
households = st.sidebar.slider("Households", 100, 5000, 400)
median_income = st.sidebar.slider("Median Income (in $10,000s)", 0.5, 15.0, 4.0)

# Ocean proximity dropdown (one-hot encoded internally)
ocean_proximity = st.sidebar.selectbox(
    "Ocean Proximity",
    ("INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND")
)

# One-hot encoding manually
ocean_proximity_INLAND = 1 if ocean_proximity == "INLAND" else 0
ocean_proximity_NEAR_OCEAN = 1 if ocean_proximity == "NEAR OCEAN" else 0
ocean_proximity_NEAR_BAY = 1 if ocean_proximity == "NEAR BAY" else 0
ocean_proximity_ISLAND = 1 if ocean_proximity == "ISLAND" else 0

# Create input array in same order as your model was trained
input_data = np.array([[
    longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
    population, households, median_income,
    ocean_proximity_INLAND, ocean_proximity_NEAR_BAY,
    ocean_proximity_NEAR_OCEAN, ocean_proximity_ISLAND
]])
import pandas as pd
# Create input DataFrame
input_data = pd.DataFrame({
    'longitude': [longitude],
    'latitude': [latitude],
    'housing_median_age': [housing_median_age],
    'total_rooms': [total_rooms],
    'total_bedrooms': [total_bedrooms],
    'population': [population],
    'households': [households],
    'median_income': [median_income],
    'ocean_proximity': [ocean_proximity]
})

# Prediction
if st.button("🔍 Predict House Price"):
    prediction = pipe.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: **${prediction:,.2f}**")

# Footer
st.markdown("---")
st.markdown("💡 *Built with Streamlit and Machine Learning by Anand.*")