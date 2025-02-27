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
    .stApp { background-color: var(--background-color); color: var(--text-color); }
    .stButton>button { background-color: #8A2BE2; color: white; border-radius: 5px; padding: 10px 20px; font-size: 16px; border: none; transition: 0.3s ease; }
    .stButton>button:hover { background-color: #7B1FA2; transform: scale(1.05); }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: var(--heading-color); text-align: center; animation: fadeIn 2s ease-in-out; font-family: 'Arial', sans-serif; }
    .stSelectbox select, .stNumberInput input { background-color: var(--input-background); color: var(--text-color); border: 1px solid #8A2BE2; }
    .stSidebar { background-color: var(--sidebar-background); color: var(--text-color); }
    [data-theme="light"] { --background-color: #ffffff; --text-color: #000000; --heading-color: #8A2BE2; --input-background: #f0f2f6; --sidebar-background: #3f3f3f; }
    [data-theme="dark"] { --background-color: #0e1117; --text-color: #ffffff; --heading-color: #8A2BE2; --input-background: #1e1e1e; --sidebar-background: #3f3f3f; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown("<h1>🌌 Infinity Unit Converter✨</h1>", unsafe_allow_html=True)
st_lottie(lottie_heading, height=200, key="heading_animation")
st.markdown("""
Welcome to the **Infinity Unit Converter**! Convert between different units of length, weight, and temperature with ease.
This app is designed and developed by Wajahat Ali🌌❤️.
""")

# Sidebar for Settings
st.sidebar.header("⚙️ Settings")
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])

# Unit Conversion History
if "history" not in st.session_state:
    st.session_state.history = []

if st.sidebar.button("Clear History"):
    st.session_state.history = []

st.sidebar.subheader("📜 Conversion History")
for item in st.session_state.history[-5:]:
    st.sidebar.text(item)

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

    length_conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Miles": 0.000621371
    }

    if st.button("Convert"):
        converted_value = value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
        result = f"✅ **{value} {from_unit} = {converted_value:.2f} {to_unit}**"
        st.session_state.history.append(result)
        st.success(result)

# Footer
st.markdown("---")
st.markdown("""
**Made by Wajahat💜✨**  
Using [Streamlit](https://streamlit.io/) for an amazing user experience.
""")
