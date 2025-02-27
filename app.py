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

# Sidebar Enhancements
with st.sidebar:
    st.image("https://i.pravatar.cc/100", caption="Wajahat Ali", width=100)
    st.title("⚙️ Settings")
    theme_toggle = st.toggle("Dark Mode")
    unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])
    st.markdown("---")
    st.subheader("Quick Links")
    st.button("📏 Length Converter")
    st.button("⚖️ Weight Converter")
    st.button("🌡 Temperature Converter")
    st.markdown("---")
    st.subheader("Recent History")
    if "history" in st.session_state and st.session_state.history:
        for item in st.session_state.history[-5:]:
            st.text(item)
    else:
        st.text("No recent conversions")
    
# Title and Introduction
st.markdown("<h1>🌌 Infinity Unit Converter✨</h1>", unsafe_allow_html=True)
st_lottie(lottie_heading, height=200, key="heading_animation")
st.markdown("""
Welcome to the **Infinity Unit Converter**! Convert between different units of length, weight, and temperature with ease.
This app is designed and developed by Wajahat Ali🌌❤️.
""")

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
        st.session_state.history.append(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        st.success(f"✅ **{value} {from_unit} = {converted_value:.2f} {to_unit}**")

# Footer
st.markdown("---")
st.markdown("""
**Made by Wajahat💜✨**  
Using [Streamlit](https://streamlit.io/) for an amazing user experience.
"")
