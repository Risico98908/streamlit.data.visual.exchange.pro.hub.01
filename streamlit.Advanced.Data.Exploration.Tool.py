#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Title of the App
st.title("InsightPro: Advanced Data Exploration Tool")

# Sidebar for file upload and user settings
st.sidebar.header("Upload Dataset and Configure Settings")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Sidebar for visualization options
chart_type = st.sidebar.radio("Choose Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram"])
selected_color = st.sidebar.color_picker("Pick a Chart Color", "#FF5733")
value_filter = st.sidebar.slider("Filter data values", 0, 100, 25)

# Session State for Storing Filtered Data
if 'filtered_data' not in st.session_state:
    st.session_state['filtered_data'] = pd.DataFrame()

# Main App Section: Data Handling and Visualization
st.header("Data Overview & Visualization")

# If file is uploaded
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview")
    st.dataframe(data.head(10))

    # Filter Column Selection
    st.sidebar.subheader("Filter Data")
    filter_column = st.sidebar.selectbox("Select column to filter", data.columns)

    # Filter data based on slider value
    filtered_data = data[data[filter_column] > value_filter]
    st.session_state['filtered_data'] = filtered_data

    st.write(f"### Filtered Data (by `{filter_column} > {value_filter}`)")
    st.dataframe(filtered_data)

    # Chart Visualization
    st.subheader(f"{chart_type} for `{filter_column}`")
    if chart_type == "Line Chart":
        st.line_chart(filtered_data[filter_column])
    elif chart_type == "Bar Chart":
        st.bar_chart(filtered_data[filter_column])
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        ax.scatter(filtered_data.index, filtered_data[filter_column], color=selected_color)
        st.pyplot(fig)
    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        ax.hist(filtered_data[filter_column], bins=20, color=selected_color)
        st.pyplot(fig)

    # Data Summary
    with st.expander("Summary Statistics"):
        st.write(filtered_data.describe())

    # Data Download
    st.subheader("Download Filtered Data")
    csv = filtered_data.to_csv(index=False)
    st.download_button("Download Filtered Data", data=csv, file_name="filtered_data.csv", mime="text/csv")

# Progress Bar Example
st.header("Simulated Data Processing Progress")
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.02)
    progress_bar.progress(i + 1)

# Metrics Section
st.header("Key Metrics from Data")
if uploaded_file:
    st.metric("Max Value", filtered_data[filter_column].max())
    st.metric("Min Value", filtered_data[filter_column].min())
    st.metric("Mean Value", round(filtered_data[filter_column].mean(), 2))

# Feedback Section
st.subheader("Feedback Section")
with st.form("feedback_form"):
    user_name = st.text_input("Your Name")
    feedback_message = st.text_area("Your Feedback")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Thank you, {user_name}, for your feedback!")
        st.write(f"Your Feedback: {feedback_message}")

# Chat Section for Collaborative Teams
st.header("Team Collaboration Chat")
chat_message = st.chat_input("Send a message to your team")
if chat_message:
    st.write(f"You: {chat_message}")
    with st.expander("Chat History"):
        st.chat_message("team_member_1").write("Team Member 1: Let's analyze this dataset further.")
        st.chat_message("team_member_2").write("Team Member 2: Agreed! This looks promising.")

# LaTeX Formula Example
st.latex(r"\sum_{i=1}^{n} x_i = X")

# Task Simulation with Spinner
st.header("Long Running Task Simulation")
with st.spinner("Simulating a long running task..."):
    time.sleep(3)
st.success("Task completed successfully!")

# Footer Section
st.markdown("---")
st.text("InsightPro © 2024 | Advanced Data Exploration Platform")
