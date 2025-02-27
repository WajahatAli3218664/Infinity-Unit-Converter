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
    
    /* Updated Title Bar Styling */
    .golden-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        padding: 15px;
        border-radius: 12px;
        background: linear-gradient(120deg, #1A237E, #311B92, #0D47A1);
        color: white;
        animation: shimmer 3s infinite;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .golden-title span {
        background: linear-gradient(90deg, #FFC107, #FFEB3B, #FFC107);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin-bottom: 1rem;
    }
    
    .title-icon {
        font-size: 2.5rem;
        margin: 0 10px;
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

    /* Main conversion button - UPDATED STYLING */
    /* Using !important to override other styles */
    button[kind="primary"] {
        background-color: #4B0082 !important; /* Indigo base color */
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        border: 2px solid #4B0082 !important;
    }
    
    button[kind="primary"]:hover {
        background-color: #00FFFF !important; /* Cyan on hover */
        color: #000000 !important;
        border-color: #00FFFF !important;
    }
    
    /* Make the button stand out with a subtle glow effect */
    button[kind="primary"] {
        position: relative !important;
    }
    
    button[kind="primary"]::after {
        content: "" !important;
        position: absolute !important;
        top: -4px !important;
        left: -4px !important;
        right: -4px !important;
        bottom: -4px !important;
        border-radius: 12px !important;
        background: linear-gradient(45deg, #4B0082, #00FFFF) !important;
        z-index: -1 !important;
        opacity: 0.3 !important;
        transition: opacity 0.3s ease !important;
    }
    
    button[kind="primary"]:hover::after {
        opacity: 0.6 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title and Introduction - UPDATED TITLE STYLING
st.markdown("""<div class="golden-title">🌌 <span>Infinity Unit Converter</span> ✨</div>""", unsafe_allow_html=True)
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
    if st.button("Convert", type="primary"):
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
    if st.button("Convert", type="primary"):
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
    if st.button("Convert", type="primary"):
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
