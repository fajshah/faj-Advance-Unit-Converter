import streamlit as st
import os


# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254}
    return value * length_units[to_unit] / length_units[from_unit]


def weight_converter(value, from_unit, to_unit):
    weight_units = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495}
    return value * weight_units[to_unit] / weight_units[from_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32


def time_converter(value, from_unit, to_unit):
    time_units = {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400}
    return value * time_units[to_unit] / time_units[from_unit]


# Streamlit UI
st.title("🌍 **Advance Unit Converter**")

# Handle icon image
icon_path = "icon.png"
if os.path.exists(icon_path):
    st.image(icon_path, width=50)

st.markdown("Convert between various units seamlessly! 🌟")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4781/4781517.png", width=100)
st.sidebar.title("🔧 Conversion Options")

conversion_type = st.sidebar.selectbox("Choose Conversion Type:", ["Length", "Weight", "Temperature", "Time"])

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day"]
}

from_unit = st.selectbox("From Unit:", units[conversion_type])
to_unit = st.selectbox("To Unit:", units[conversion_type])
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

if st.button("🚀 Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "Time":
        result = time_converter(value, from_unit, to_unit)

    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

st.info("Supports length, weight, temperature, and time conversions. Real-time results! 💡")

# Footer
st.markdown("""
---
👩‍💻 **Made by Syeda Farzana Shah**

🔗 [GitHub](#) | 📧 [Email](#) | 🌍 [Website](#)
""")
