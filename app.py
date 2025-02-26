import streamlit as st # type: ignore
from streamlit_lottie import st_lottie # type: ignore
import requests # type: ignore

# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except requests.exceptions.RequestException:
        return None
    return None

# Load Lottie animations
lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6wutsrox.json")
lottie_heading = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_2cwDXD.json")

# Title and Introduction
st.markdown("""
    <h1 style='text-align: center; color: #8A2BE2;'>🌌 Infinity Unit Converter✨</h1>
""", unsafe_allow_html=True)
if lottie_heading:
    st_lottie(lottie_heading, height=200, key="heading_animation")

st.markdown("""
Welcome to the **Infinity Unit Converter**! Convert between different units of length, weight, and temperature with ease.
This app is designed and developed by **Wajahat Ali** 🌌❤️.
""")

if lottie_animation:
    st_lottie(lottie_animation, height=300, key="unit_converter")

# Sidebar settings
st.sidebar.header("⚙️ Settings")
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

# Initialize history if not present
if "history" not in st.session_state:
    st.session_state.history = []

# Conversion dictionaries
conversion_factors = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Feet": 3.28084, "Inches": 39.3701, "Miles": 0.000621371},
    "Weight": {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
}

def convert_units(value, from_unit, to_unit, category):
    factor = conversion_factors[category]
    return value * (factor[to_unit] / factor[from_unit])

# Conversion logic
st.header(f"{unit_type} Converter")

if unit_type in ["Length", "Weight"]:
    units = list(conversion_factors[unit_type].keys())
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, unit_type)
        st.session_state.history.append(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", format="%.2f")

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
        elif from_unit == "Fahrenheit":
            return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
        elif from_unit == "Kelvin":
            return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.session_state.history.append(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Conversion history in sidebar
st.sidebar.header("📜 Conversion History")
st.sidebar.write("\n".join(st.session_state.history[-5:]))

st.markdown("---")
st.markdown("**Made by Wajahat Ali💜✨** Using [Streamlit](https://streamlit.io/)")