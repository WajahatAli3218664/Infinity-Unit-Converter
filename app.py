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

# Custom CSS for both light and dark themes
st.markdown("""
<style>
    /* General styles */
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stButton>button {
        background-color: #8A2BE2; /* Purple color */
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #7B1FA2; /* Darker purple on hover */
        transform: scale(1.05);
    }
    .stMarkdown h1 {
        color: var(--heading-color);
        text-align: center;
        animation: bounce 2s infinite, fadeIn 2s ease-in-out, scale 3s infinite;
        font-family: 'Arial', sans-serif;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }
    .stMarkdown h2 {
        color: var(--heading-color);
        animation: slideIn 1s ease-in-out;
    }
    .stMarkdown h3 {
        color: var(--heading-color);
        animation: fadeIn 1.5s ease-in-out;
    }
    .stSelectbox>div>div>select {
        background-color: var(--input-background);
        color: var(--text-color);
        border: 1px solid #8A2BE2; /* Purple border */
    }
    .stNumberInput>div>div>input {
        background-color: var(--input-background);
        color: var(--text-color);
        border: 1px solid #8A2BE2; /* Purple border */
    }
    .stSuccess {
        background: linear-gradient(135deg, #FF6F61, #8A2BE2); /* Gradient from pink to purple */
        color: white;
        padding: 10px;
        border-radius: 5px;
        animation: fadeIn 1s ease-in-out;
    }

    /* Sidebar styles */
    .stSidebar {
        background-color: var(--sidebar-background);
        color: var(--text-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stSidebar .stMarkdown {
        font-size: 16px;
        color: var(--text-color);
    }
    .stSidebar .stMarkdown h1, .stSidebar .stMarkdown h2, .stSidebar .stMarkdown h3 {
        color: var(--heading-color);
    }

    /* Mobile-specific styles */
    @media (max-width: 768px) {
        .stSidebar {
            width: 100% !important; /* Full width on mobile */
            padding: 15px;
            border-radius: 0; /* Remove border radius for full-width mobile view */
            box-shadow: none; /* Remove shadow for full-width mobile view */
            margin-bottom: 20px; /* Add space below the sidebar */
        }
        .stSidebar .stMarkdown {
            font-size: 14px; /* Smaller font size for mobile */
        }
        .stSidebar .stMarkdown h1 {
            font-size: 1.5rem; /* Smaller heading size for mobile */
        }
        .stSidebar .stMarkdown h2 {
            font-size: 1.25rem; /* Smaller heading size for mobile */
        }
        .stSidebar .stMarkdown h3 {
            font-size: 1rem; /* Smaller heading size for mobile */
        }
        /* Prevent overlap with main content */
        .stApp > div:first-child {
            padding-top: 20px; /* Add padding to the top of the main content */
        }
    }

    /* Light theme variables */
    [data-theme="light"] {
        --background-color: #ffffff;
        --text-color: #000000;
        --heading-color: #8A2BE2; /* Purple heading */
        --input-background: #f0f2f6;
        --sidebar-background: #f0f2f6;
    }

    /* Dark theme variables */
    [data-theme="dark"] {
        --background-color: #0e1117;
        --text-color: #ffffff;
        --heading-color: #8A2BE2; /* Purple heading */
        --input-background: #1e1e1e;
        --sidebar-background: #1e1e1e;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-20px);
        }
        60% {
            transform: translateY(-10px);
        }
    }
    @keyframes scale {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
        }
    }
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown("<h1>🌌 Infinity Unit Converter✨</h1>", unsafe_allow_html=True)
st_lottie(lottie_heading, height=200, key="heading_animation")
st.markdown("""
Welcome to the **Infinity Unit Converter**! Convert between different units of length, weight, and temperature with ease.
This app is designed and developed by Wajahat Ali🌌❤️.
""")

# Add Lottie animation
st_lottie(lottie_animation, height=300, key="unit_converter")

# Sidebar for unit selection
st.sidebar.header("⚙️ Settings")
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

# New Feature: Unit History
if "history" not in st.session_state:
    st.session_state.history = []

# Conversion logic
if unit_type == "Length":
    st.header("📏 Length Converter")
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Miles"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", length_units)
    with col2:
        to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")

    # Conversion factors
    length_conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Miles": 0.000621371
    }

    if st.button("Convert"):
        converted_value = value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ **{value} {from_unit} = {converted_value:.2f} {to_unit}**")

elif unit_type == "Weight":
    st.header("⚖️ Weight Converter")
    weight_units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", weight_units)
    with col2:
        to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")

    # Conversion factors
    weight_conversion_factors = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274
    }

    if st.button("Convert"):
        converted_value = value * (weight_conversion_factors[to_unit] / weight_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ **{value} {from_unit} = {converted_value:.2f} {to_unit}**")

elif unit_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", temp_units)
    with col2:
        to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter value", min_value=-273.15, format="%.2f")

    # Conversion logic
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            converted_value = (value * 9/5) + 32
        elif to_unit == "Kelvin":
            converted_value = value + 273.15
        else:
            converted_value = value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            converted_value = (value - 32) * 5/9
        elif to_unit == "Kelvin":
            converted_value = (value - 32) * 5/9 + 273.15
        else:
            converted_value = value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            converted_value = value - 273.15
        elif to_unit == "Fahrenheit":
            converted_value = (value - 273.15) * 9/5 + 32
        else:
            converted_value = value

    if st.button("Convert"):
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ **{value} {from_unit} = {converted_value:.2f} {to_unit}**")

# New Feature: Display Conversion History
st.sidebar.header("📜 Conversion History")
if st.session_state.history:
    for entry in st.session_state.history:
        st.sidebar.write(entry)
else:
    st.sidebar.write("No conversions yet.")

# Footer
st.markdown("---")
st.markdown("""
**Made by Wajahat Ali💜✨**  
Using [Streamlit](https://streamlit.io/) for an amazing user experience.
""")
