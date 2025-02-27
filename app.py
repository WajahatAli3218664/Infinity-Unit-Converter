import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6wutsrox.json")

# Sidebar toggle state
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = True

def toggle_sidebar():
    st.session_state.sidebar_state = not st.session_state.sidebar_state

# Sidebar toggle button
st.sidebar.button("☰ Toggle Sidebar", on_click=toggle_sidebar)

if st.session_state.sidebar_state:
    with st.sidebar:
        st.header("⚙️ Settings")
        unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])
else:
    unit_type = None

# Page title & animation
st.markdown("<h1 style='text-align: center;'>🌌 Infinity Unit Converter✨</h1>", unsafe_allow_html=True)
st_lottie(lottie_animation, height=200, key="unit_converter")

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361,
        "Foot": 3.28084, "Inch": 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Unit conversion UI
if unit_type:
    st.subheader(f"🔢 {unit_type} Converter")
    
    if unit_type == "Length":
        units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    elif unit_type == "Weight":
        units = ["Kilogram", "Gram", "Pound", "Ounce"]
    else:
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    
    if st.button("Convert"):  
        if unit_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif unit_type == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        else:
            result = convert_temperature(value, from_unit, to_unit)
        
        st.success(f"Converted Value: {result:.2f} {to_unit}")

# Custom CSS for Sidebar Animation
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        transition: all 0.3s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)
