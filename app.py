import streamlit as st

# Unit conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    return value * length_units[to_unit] / length_units[from_unit]


def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1e6,
        "pounds": 2.20462,
        "ounces": 35.274,
    }
    return value * weight_units[to_unit] / weight_units[from_unit]


def temperature_conversion(value, from_unit, to_unit):
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
    if to_unit == "Fahrenheit" and from_unit == "Kelvin":
        return (value - 273.15) * 9/5 + 32


# Streamlit UI with sidebar and colors
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🌍", layout="wide")

st.sidebar.header("Navigation 🧭")
st.sidebar.write("Choose your options below:")

category = st.sidebar.selectbox("Select a category", [
    "📏 Length", "⚖️ Weight", "🌡️ Temperature"
])
value = st.sidebar.number_input("Enter the value to convert", min_value=0.0)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        color: #FF6F61;
    }
    .result-card {
        background-color: #E3FCEF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 1em;
        color: red;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌍 Advanced Unit Converter</div>", unsafe_allow_html=True)

st.write("Convert between different units with ease. Just select a category, enter a value, and get your result instantly! 💡")

if category == "📏 Length":
    length_units = [
        "meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"
    ]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    result = length_conversion(value, from_unit, to_unit)

elif category == "⚖️ Weight":
    weight_units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    result = weight_conversion(value, from_unit, to_unit)

elif category == "🌡️ Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    result = temperature_conversion(value, from_unit, to_unit)

if st.button("Convert 🚀"):
    st.markdown(f"<div class='result-card'><h3>Result: {result} {to_unit}</h3></div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Made with ❤️ by Syeda Farzana Shah</div>", unsafe_allow_html=True)
