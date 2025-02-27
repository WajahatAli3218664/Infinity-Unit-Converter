import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6wutsrox.json")

# Custom CSS
st.markdown("""
<style>
    @keyframes glow {
        0% { color: #FFD700; text-shadow: 0 0 5px #FFD700; }
        50% { color: #FFA500; text-shadow: 0 0 10px #FFA500; }
        100% { color: #FFD700; text-shadow: 0 0 5px #FFD700; }
    }
    .golden-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        animation: glow 2s infinite alternate;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #357ABD;
        transform: scale(1.05);
    }
    .history-box {
        background-color: #222;
        padding: 10px;
        border-radius: 5px;
        color: white;
        font-size: 14px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="golden-title">🌌 Infinity Unit Converter✨</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Settings")
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

# History Feature
st.sidebar.header("📜 Conversion History")
if "history" not in st.session_state:
    st.session_state.history = []
if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
for entry in st.session_state.history:
    st.sidebar.markdown(f'<div class="history-box">{entry}</div>', unsafe_allow_html=True)

# Conversion logic
if unit_type == "Length":
    st.header("📏 Length Converter")
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Miles"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")

    length_conversion_factors = {"Meters": 1, "Kilometers": 0.001, "Feet": 3.28084, "Inches": 39.3701, "Miles": 0.000621371}

    if st.button("Convert"):
        converted_value = value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")

elif unit_type == "Weight":
    st.header("⚖️ Weight Converter")
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")

    weight_conversion_factors = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}

    if st.button("Convert"):
        converted_value = value * (weight_conversion_factors[to_unit] / weight_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")

elif unit_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter value", format="%.2f")

    def convert_temp(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
        if from_unit == "Fahrenheit":
            return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
        if from_unit == "Kelvin":
            return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)

    if st.button("Convert"):
        converted_value = convert_temp(value, from_unit, to_unit)
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")
