#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np
import time

# App Title
st.title("Advanced Data Analysis and Visualization Dashboard")

# Sidebar for file upload and input widgets
st.sidebar.header("Upload and Customize")

# File uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Sidebar settings for visualization
chart_type = st.sidebar.radio("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart", "Scatter Chart"])
color = st.sidebar.color_picker("Pick a chart color", "#FF6347")
value_filter = st.sidebar.slider("Filter Values (Minimum)", 0, 100, 50)

# Sidebar settings for metrics and progress
show_metrics = st.sidebar.checkbox("Show Data Metrics")
progress_display = st.sidebar.checkbox("Show Progress")

# Header and introduction text
st.header("Data Overview")
st.markdown("This dashboard allows users to upload datasets, filter the data, and visualize it using various chart types. Explore your data dynamically!")

# If file is uploaded
if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Displaying the first few rows of the dataset
    st.subheader("Preview of Uploaded Data")
    st.dataframe(data.head())

    # Select column for filtering and visualization
    selected_column = st.selectbox("Select a column to visualize", data.columns)

    # Filter data based on user selection
    filtered_data = data[data[selected_column] > value_filter]
    st.write(f"Filtered Data for `{selected_column}` > {value_filter}")
    st.dataframe(filtered_data)

    # Display selected chart type
    st.subheader(f"{chart_type} of `{selected_column}`")
    if chart_type == "Line Chart":
        st.line_chart(filtered_data[selected_column])
    elif chart_type == "Bar Chart":
        st.bar_chart(filtered_data[selected_column])
    elif chart_type == "Area Chart":
        st.area_chart(filtered_data[selected_column])
    else:
        st.scatter_chart(filtered_data[selected_column])

    # Show data metrics if checkbox is selected
    if show_metrics:
        st.subheader("Data Metrics")
        st.metric("Maximum Value", filtered_data[selected_column].max())
        st.metric("Minimum Value", filtered_data[selected_column].min())
        st.metric("Mean Value", round(filtered_data[selected_column].mean(), 2))

    # Display summary statistics in an expander
    with st.expander("Show Summary Statistics"):
        st.write(filtered_data.describe())

    # Display progress bar if selected
    if progress_display:
        st.subheader("Data Processing Progress")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.05)
            progress_bar.progress(percent_complete + 1)

    # Add LaTeX formula for fun
    st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

    # Button to trigger analysis completion
    if st.button("Complete Analysis"):
        st.success("Analysis completed successfully!")
        st.balloons()

# Instructions if no file is uploaded
else:
    st.warning("Please upload a CSV file to get started.")
    st.markdown("""
        **Instructions:**
        1. Upload your dataset using the sidebar.
        2. Customize the filters and chart types.
        3. View metrics, progress, and results dynamically.
    """)

# Footer
st.text("Data Analysis Dashboard © 2024")

# Additional Section with Chat Elements
st.header("Live Data Chat and Feedback")
st.write("You can chat with your team about this data analysis below:")

# Chat input and messages
chat_message = st.chat_input("Send a message")
if chat_message:
    st.chat_message("user").write(f"You: {chat_message}")

# Footer disclaimer
st.markdown("""
---
*Note: This dashboard can be improved.*
""")
