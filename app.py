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

# Load Lottie animations
lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6wutsrox.json")
lottie_heading = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_2cwDXD.json")

# Initialize session state variables
if "history" not in st.session_state:
    st.session_state.history = []
if "total_conversions" not in st.session_state:
    st.session_state.total_conversions = 0
if "most_active_category" not in st.session_state:
    st.session_state.most_active_category = "None"
if "feedback_count" not in st.session_state:
    st.session_state.feedback_count = 0
if "session_start" not in st.session_state:
    st.session_state.session_start = time.time()

# Custom CSS for styling
st.markdown("""
<style>
    /* General styles for both themes */
    .stApp {
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover {
        transform: scale(1.08);
    }
    .golden-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    .golden-title span {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .footer {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 40px;
    }
    .footer p {
        margin: 0;
        font-size: 1.1rem;
    }
    .footer .quote {
        font-style: italic;
        margin-bottom: 10px;
    }
    .footer .signature {
        font-weight: bold;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Light theme */
    [data-theme="light"] {
        background-color: #ffffff;
        color: #000000;
    }
    [data-theme="light"] .stButton>button {
        background-color: #ff9800;
        color: white;
    }
    [data-theme="light"] .stButton>button:hover {
        background-color: #013220;
        color: white;
    }
    [data-theme="light"] .footer {
        background-color: #f3f4f6;
        color: #000000;
    }
    [data-theme="light"] .footer .quote {
        color: #6b7280;
    }
    [data-theme="light"] .footer .signature {
        color: #ff9800;
    }

    /* Dark theme */
    [data-theme="dark"] {
        background-color: #0e1117;
        color: white;
    }
    [data-theme="dark"] .stButton>button {
        background-color: #ff9800;
        color: white;
    }
    [data-theme="dark"] .stButton>button:hover {
        background-color: #013220;
        color: white;
    }
    [data-theme="dark"] .footer {
        background-color: #1f2937;
        color: #f3f4f6;
    }
    [data-theme="dark"] .footer .quote {
        color: #9ca3af;
    }
    [data-theme="dark"] .footer .signature {
        color: #ff9800;
    }

    /* Sidebar buttons */
    .stSidebar .stButton>button {
        background-color: #800080; /* Purple */
        color: white;
    }
    .stSidebar .stButton>button:hover {
        background-color: #4B0082; /* Darker purple on hover */
        color: white;
    }

    /* Main conversion button */
    .stButton>button.convert-button {
        background-color: #4B0082; /* Indigo */
        color: white;
        font-weight: bold;
    }
    .stButton>button.convert-button:hover {
        background-color: #00FFFF; /* Cyan on hover */
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown("""<h1 class='golden-title'>🌌 <span>Infinity Unit Converter</span> ✨</h1>""", unsafe_allow_html=True)
st_lottie(lottie_heading, height=200, key="heading_animation")

st.markdown("""
Welcome to the **Infinity Unit Converter**! Convert between different units of length, weight, and temperature with ease.
This app is designed and developed by Wajahat Ali🌌❤️.
""")

st_lottie(lottie_animation, height=300, key="unit_converter")

# Sidebar Sections
st.sidebar.header("🌟 Pro Tips")
st.sidebar.info("""
💡 Check history for recent conversions

⚡ Use Clear History to reset all stats

📊 Track your most used conversions

💭 Share feedback to improve the app

🎯 View stats to monitor usage
""")

st.sidebar.header("📊 Live Stats")
session_duration = int(time.time() - st.session_state.session_start)
st.sidebar.write(f"⏰ Session Duration: {session_duration//60:02}:{session_duration%60:02}:00")
st.sidebar.write(f"🔄 Total Conversions: {st.session_state.total_conversions}")
st.sidebar.write(f"💭 Feedback Count: {st.session_state.feedback_count}")
st.sidebar.write(f"📈 Most Active Category: {st.session_state.most_active_category}")

# Conversion history
total_conversions = len(st.session_state.history)
st.sidebar.header("📜 Conversion History")
if st.sidebar.button("Clear History"):
    st.session_state.history = []
    st.session_state.total_conversions = 0
for entry in st.session_state.history:
    st.sidebar.write(entry)

# Feedback section
st.sidebar.header("💬 Feedback")
feedback = st.sidebar.text_area("Share your thoughts or suggestions:")
if st.sidebar.button("Submit Feedback"):
    if feedback:
        st.session_state.feedback_count += 1
        st.sidebar.success("Thank you for your feedback! 😊")

# Unit Conversion Section
unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

if unit_type == "Length":
    st.header("📏 Length Converter")
    st.session_state.most_active_category = "Length"
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Miles"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    length_conversion_factors = {"Meters": 1, "Kilometers": 0.001, "Feet": 3.28084, "Inches": 39.3701, "Miles": 0.000621371}
    if st.button("Convert", key="length_convert", help="Convert length units"):
        converted_value = value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.session_state.total_conversions += 1
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")

elif unit_type == "Weight":
    st.header("⚖️ Weight Converter")
    st.session_state.most_active_category = "Weight"
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    weight_conversion_factors = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    if st.button("Convert", key="weight_convert", help="Convert weight units"):
        converted_value = value * (weight_conversion_factors[to_unit] / weight_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.session_state.total_conversions += 1
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")

elif unit_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    st.session_state.most_active_category = "Temperature"
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    value = st.number_input("Enter value", format="%.2f")
    if st.button("Convert", key="temp_convert", help="Convert temperature units"):
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
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.session_state.total_conversions += 1
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")

# Footer Section
st.markdown("""
<div class="footer">
    <p class="quote">"The only limit to our realization of tomorrow is our doubts of today."</p>
    <p class="signature">Designed by Wajahat Ali</p>
</div>   
""", unsafe_allow_html=True)
