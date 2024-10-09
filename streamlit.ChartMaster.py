import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Interactive Data Dashboard")

# Sidebar for file upload and chart options
st.sidebar.header("User Input")
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])
chart_type = st.sidebar.radio("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

# Slider to filter data
filter_value = st.sidebar.slider("Filter Value", 0, 100, 50)

# Sidebar color picker for customizing chart color
chart_color = st.sidebar.color_picker("Pick a chart color")

# Checkbox to show/hide additional data
show_additional = st.sidebar.checkbox("Show additional data")

# Display DataFrame when file is uploaded
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview")
    st.dataframe(data)

    # Selectbox to choose column for visualization
    column = st.selectbox("Choose a column to visualize", data.columns)

    # Filter data based on slider
    filtered_data = data[data[column] > filter_value]

    # Display the filtered data
    st.write(f"Data filtered by {column} > {filter_value}")
    st.table(filtered_data)

    # Display chosen chart type
    if chart_type == "Line Chart":
        st.line_chart(filtered_data[column])
    elif chart_type == "Bar Chart":
        st.bar_chart(filtered_data[column])
    else:
        st.scatter_chart(filtered_data[column])

    # Display progress bar
    st.progress(int(filtered_data[column].mean()))

    # Show additional data if checkbox is checked
    if show_additional:
        st.write("Additional Data Information:")
        st.write(filtered_data.describe())

    # Show success message on analysis
    if st.button("Complete Analysis"):
        st.success("Analysis Complete!")
        st.balloons()

    # LaTeX display
    st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

# Footer text
st.text("Data Dashboard App © 2024")
