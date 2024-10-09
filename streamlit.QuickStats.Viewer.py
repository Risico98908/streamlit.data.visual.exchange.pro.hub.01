#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("Interactive Data Analysis Tool")

# Sidebar for file upload and settings
st.sidebar.header("Input Settings")
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])

# Sidebar radio for chart type selection
chart_type = st.sidebar.radio("Choose chart type", ["Line", "Bar", "Scatter"])

# Sidebar slider for value filter
filter_value = st.sidebar.slider("Filter data values", 0, 100, 50)

# Sidebar color picker
chart_color = st.sidebar.color_picker("Pick a chart color", "#FF6347")

# Main content
st.header("Data Display and Visualization")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    selected_column = st.selectbox("Select a column for visualization", data.columns)
    filtered_data = data[data[selected_column] > filter_value]

    st.subheader(f"Filtered Data for {selected_column} > {filter_value}")
    st.write(filtered_data)

    # Displaying selected chart type
    if chart_type == "Line":
        st.line_chart(filtered_data[selected_column])
    elif chart_type == "Bar":
        st.bar_chart(filtered_data[selected_column])
    else:
        st.scatter_chart(filtered_data[selected_column])

    # Expander for summary statistics
    with st.expander("Show summary statistics"):
        st.write(filtered_data.describe())

    # Progress bar and metric display
    st.progress(int(filtered_data[selected_column].mean()))
    st.metric(label="Max Value", value=f"{filtered_data[selected_column].max()}")

    # Button and success message
    if st.button("Run Analysis"):
        st.success("Analysis completed successfully!")
        st.balloons()

    # Display LaTeX formula
    st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

# Footer text
st.text("Data Analysis App © 2024")
