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
        st.success(f"✅ **{
