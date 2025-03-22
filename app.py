import streamlit as st
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Streamlit App
st.title("Simple Bar Chart in Streamlit")

# Show DataFrame
st.write("### Data Preview")
st.dataframe(df)  # Using st.dataframe() instead of st.write(df) for better display

# Add spacing
st.write("")  # Empty line
st.write("")  # Another empty line
st.divider()  # Horizontal line for better separation
st.write("")  # More space after the divider

# Bar Chart
st.write("### Bar Chart")
st.bar_chart(df.set_index('first column'))
