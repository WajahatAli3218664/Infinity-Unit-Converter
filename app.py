import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6wutsrox.json")
lottie_heading = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_2cwDXD.json")

# Title and Introduction
st.markdown("""
    <h1 style='text-align: center; color: #8A2BE2;'>🌌 Infinity Unit Converter✨</h1>
""", unsafe_allow_html=True)
st_lottie(lottie_heading, height=200, key="heading_animation")

st.markdown("""
Welcome to the **Infinity Unit Converter**! Convert between different units of **Length, Weight, and Temperature** with ease.
This app is designed and developed by **Wajahat Ali🌌❤️**.
""")

# Add Lottie animation
st_lottie(lottie_animation, height=300, key="unit_converter")

# Sidebar for unit selection and history
st.sidebar.header("⚙️ Settings")
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

# Conversion history in the sidebar
st.sidebar.header("📜 Conversion History")
if "history" not in st.session_state:
    st.session_state.history = []

if st.sidebar.button("Clear History"):
    st.session_state.history = []

for entry in reversed(st.session_state.history):  # Show latest conversions first
    st.sidebar.write(entry)

# Conversion logic
if unit_type == "Length":
    st.header("📏 Length Converter")
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Miles"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", length_units, key="length_from")
    with col2:
        to_unit = st.selectbox("To", length_units, key="length_to")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f", key="length_value")

    length_conversion_factors = {
        "Meters": 1, "Kilometers": 0.001, "Feet": 3.28084, "Inches": 39.3701, "Miles": 0.000621371
    }

    if st.button("Convert Length"):
        converted_value = value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
        result = f"{value} {from_unit} = {converted_value:.2f} {to_unit}"
        st.session_state.history.append(result)
        st.success(f"✅ **{result}**")

elif unit_type == "Weight":
    st.header("⚖️ Weight Converter")
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", weight_units, key="weight_from")
    with col2:
        to_unit = st.selectbox("To", weight_units, key="weight_to")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f", key="weight_value")

    weight_conversion_factors = {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
    }

    if st.button("Convert Weight"):
        converted_value = value * (weight_conversion_factors[to_unit] / weight_conversion_factors[from_unit])
        result = f"{value} {from_unit} = {converted_value:.2f} {to_unit}"
        st.session_state.history.append(result)
        st.success(f"✅ **{result}**")

elif unit_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", temp_units, key="temp_from")
    with col2:
        to_unit = st.selectbox("To", temp_units, key="temp_to")
    value = st.number_input("Enter value", format="%.2f", key="temp_value")

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return None

    if st.button("Convert Temperature"):
        converted_value = convert_temperature(value, from_unit, to_unit)
        result = f"{value} {from_unit} = {converted_value:.2f} {to_unit}"
        st.session_state.history.append(result)
        st.success(f"✅ **{result}**")

# Footer
st.markdown("---")
st.markdown("""
**Made by Wajahat💜✨**  
Using [Streamlit](https://streamlit.io/) for an amazing user experience.
""")
