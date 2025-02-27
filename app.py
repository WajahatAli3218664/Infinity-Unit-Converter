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
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #ff9800;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #013220;  /* Green on hover */
        transform: scale(1.08);
    }
    .golden-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        font-family: 'Arial', sans-serif;
        animation: fadeIn 2s ease-in-out;
    }
    .golden-title span {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stSidebar .stButton>button {
        background-color: #6a1b9a;
        color: white;
        border-radius: 8px;
        padding: 10px 15px;
        font-size: 14px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stSidebar .stButton>button:hover {
        background-color: #4a148c;
        transform: scale(1.05);
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
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
    if st.button("Convert"):
        converted_value = value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.session_state.total_conversions += 1
        st.success(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")

st.markdown("---")
st.markdown("**Made by Wajahat💜✨**")
