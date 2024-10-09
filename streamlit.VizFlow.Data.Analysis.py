#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Dynamic Data Visualization Dashboard")

# Sidebar for file upload and settings
st.sidebar.header("Configuration Panel")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

# Sidebar widgets for chart and filters
chart_type = st.sidebar.radio("Select Chart Type", ["Bar", "Line", "Area"])
min_value = st.sidebar.slider("Minimum Value Filter", 0, 100, 25)

# Sidebar color picker
chart_color = st.sidebar.color_picker("Select Chart Color")

# Main content
st.header("Dataset and Charts")

# If file is uploaded, display data
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Overview")
    st.dataframe(data)

    # Column selection
    selected_column = st.selectbox("Select a column to visualize", data.columns)

    # Apply minimum value filter
    filtered_data = data[data[selected_column] > min_value]
    st.subheader(f"Filtered {selected_column} Data (>{min_value})")
    st.write(filtered_data)

    # Display chart based on user selection
    if chart_type == "Bar":
        st.bar_chart(filtered_data[selected_column])
    elif chart_type == "Line":
        st.line_chart(filtered_data[selected_column])
    else:
        st.area_chart(filtered_data[selected_column])

    # Expander for detailed statistics
    with st.expander("Show Statistics"):
        st.write(filtered_data.describe())

    # Progress bar and metrics
    st.progress(int(filtered_data[selected_column].mean()))
    st.metric(label="Max Value", value=f"{filtered_data[selected_column].max()}")

    # LaTeX formula
    st.latex(r"a^2 + b^2 = c^2")

    # Button to trigger analysis
    if st.button("Run Analysis"):
        st.success("Analysis Complete!")
        st.balloons()

# Footer
st.text("Dashboard App © 2024")
