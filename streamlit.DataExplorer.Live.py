#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Interactive Data Filtering and Visualization")

# Sidebar for uploading files
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])

# Sidebar for chart selection and value filter
chart_type = st.sidebar.radio("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
filter_value = st.sidebar.slider("Select minimum value for filtering", 0, 100, 30)

# Sidebar for selecting a color for the chart
chart_color = st.sidebar.color_picker("Select a chart color")

# Main app content
st.header("Dataset Overview")

# If file is uploaded
if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Show data
    st.write("Here is the dataset you uploaded:")
    st.dataframe(data)

    # Filter data based on slider value
    selected_column = st.selectbox("Select a column to filter and visualize", data.columns)
    filtered_data = data[data[selected_column] > filter_value]

    st.write(f"Filtered data where `{selected_column}` > {filter_value}")
    st.dataframe(filtered_data)

    # Display chart based on the user's selection
    st.subheader(f"{chart_type} for {selected_column}")
    if chart_type == "Line Chart":
        st.line_chart(filtered_data[selected_column])
    elif chart_type == "Bar Chart":
        st.bar_chart(filtered_data[selected_column])
    else:
        st.area_chart(filtered_data[selected_column])

    # Metrics and progress
    st.metric(label="Maximum Value", value=f"{filtered_data[selected_column].max()}")
    st.progress(int(filtered_data[selected_column].mean()))

    # Expander for summary statistics
    with st.expander("Show Summary Statistics"):
        st.write(filtered_data.describe())

    # Success button with balloons
    if st.button("Complete Analysis"):
        st.success("Analysis complete!")
        st.balloons()

    # LaTeX Formula
    st.latex(r"a^2 + b^2 = c^2")

# Footer
st.text("Interactive Data App © 2024")
