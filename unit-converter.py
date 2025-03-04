import streamlit as st

# Function to convert units
def convert_units(value, from_unit, to_unit):
    # Define conversion factors
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        'miles': 0.000621371
    }
    
    # Convert the input value to meters first
    if from_unit in conversion_factors:
        value_in_meters = value / conversion_factors[from_unit]
        # Convert from meters to the target unit
        return value_in_meters * conversion_factors[to_unit]
    else:
        return None

# Streamlit app layout
st.title("Simple Unit Converter")
st.write("### Convert between different units of length.")

# User input for value
value = st.number_input("Enter the value to convert:", min_value=0.0)

# User input for from_unit
from_unit = st.selectbox("From unit:", 
                          options=['meters', 'kilometers', 'centimeters', 
                                   'millimeters', 'inches', 'feet', 
                                   'yards', 'miles'])

# User input for to_unit
to_unit = st.selectbox("To unit:", 
                        options=['meters', 'kilometers', 'centimeters', 
                                 'millimeters', 'inches', 'feet', 
                                 'yards', 'miles'])

# Button to perform conversion
if st.button("Convert"):
    if value is not None:
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        else:
            st.error("Invalid unit selected.")
    else:
        st.error("Please enter a valid number.")