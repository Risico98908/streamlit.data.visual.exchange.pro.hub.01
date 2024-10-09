#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Title and header for the app
st.title("DataViz Pro: Interactive Data Analysis Hub")
st.header("Explore, Visualize, and Collaborate on Data")

# Sidebar for file upload and configuration
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Sidebar for chart type and settings
st.sidebar.subheader("Visualization Settings")
chart_type = st.sidebar.radio("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart", "Pie Chart"])
color_picker = st.sidebar.color_picker("Pick a chart color", "#00f900")
filter_value = st.sidebar.slider("Minimum Value Filter", 0, 100, 50)

# Sidebar checkbox to show/hide chat section
collaboration_mode = st.sidebar.checkbox("Enable Collaboration Mode")

# Sidebar feedback section
with st.sidebar.expander("Submit Your Feedback"):
    feedback = st.text_area("Write your feedback here")
    if st.button("Submit Feedback"):
        st.sidebar.success("Thank you for your feedback!")

# Load data if file is uploaded
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview")
    st.dataframe(data.head(10))

    # Filter data based on user input
    filter_column = st.selectbox("Select Column to Filter", data.columns)
    filtered_data = data[data[filter_column] > filter_value]
    st.write(f"Filtered Data (where `{filter_column}` > {filter_value})")
    st.dataframe(filtered_data)

    # Visualization of filtered data
    st.subheader(f"{chart_type} for {filter_column}")
    if chart_type == "Line Chart":
        st.line_chart(filtered_data[filter_column], height=400, use_container_width=True)
    elif chart_type == "Bar Chart":
        st.bar_chart(filtered_data[filter_column], height=400, use_container_width=True)
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        ax.scatter(filtered_data.index, filtered_data[filter_column], color=color_picker)
        st.pyplot(fig)
    elif chart_type == "Area Chart":
        st.area_chart(filtered_data[filter_column], height=400, use_container_width=True)
    elif chart_type == "Pie Chart":
        pie_data = filtered_data[filter_column].value_counts()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=[color_picker])
        st.pyplot(fig)

    # Expander for data summary statistics
    with st.expander("Summary Statistics"):
        st.write(filtered_data.describe())

    # Option to download filtered data
    st.subheader("Download Filtered Data")
    csv = filtered_data.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="filtered_data.csv", mime="text/csv")

# Simulating data processing with progress bar
st.header("Data Processing Progress")
with st.spinner("Processing your data..."):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)
st.success("Data processing completed!")

# Metrics visualization
st.header("Key Metrics")
if uploaded_file:
    st.metric("Maximum Value", filtered_data[filter_column].max())
    st.metric("Minimum Value", filtered_data[filter_column].min())
    st.metric("Mean Value", round(filtered_data[filter_column].mean(), 2))

# Collaboration Mode Section
if collaboration_mode:
    st.header("Collaborative Analysis and Feedback")
    chat_message = st.chat_input("Send a message to the team")
    if chat_message:
        st.write(f"You: {chat_message}")
    with st.expander("Chat History"):
        st.chat_message("Analyst1").write("Analyst1: Let's review the outliers.")
        st.chat_message("Analyst2").write("Analyst2: I agree! The patterns are interesting.")

# Latex Formula Display Example
st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

# Long-running task simulation with spinner
st.header("Running Advanced Analysis")
with st.spinner("Performing complex computations..."):
    time.sleep(3)
st.success("Advanced analysis completed!")

# Footer Section
st.markdown("---")
st.text("DataViz Pro © 2024 | Empowering Data-Driven Decisions")
