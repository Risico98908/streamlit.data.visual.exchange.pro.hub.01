#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# User Authentication Simulation
def authenticate_user(username, password):
    # Dummy authentication (can be extended with a real user database)
    if username == "admin" and password == "password123":
        return True
    return False

# Session State Setup
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Title of the App
st.title("Collaborative Data Analytics Tool")

# User Authentication Form
if not st.session_state.authenticated:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.success("Login successful")
        else:
            st.error("Invalid credentials")
    st.stop()  # Stop app until user is authenticated

# Sidebar Configuration
st.sidebar.header("User Settings")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
chart_type = st.sidebar.radio("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram", "Pie Chart"])
filter_column = st.sidebar.text_input("Filter column (by name)")
filter_value = st.sidebar.slider("Filter values greater than", 0, 100, 50)
color = st.sidebar.color_picker("Pick a color", "#FF6347")

# Sidebar settings for user collaboration options
collaboration_mode = st.sidebar.checkbox("Enable Collaboration Mode")
if collaboration_mode:
    st.sidebar.info("Collaboration Mode: Live updates and real-time chat enabled.")

# Session-based Persistent Data Settings
if 'filtered_data' not in st.session_state:
    st.session_state.filtered_data = pd.DataFrame()

# Main App Section
st.header("Data Overview & Visualization")

if uploaded_file:
    # Read the uploaded file
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data")
    st.dataframe(data.head(10))

    # Column selection and filtering
    if filter_column and filter_column in data.columns:
        filtered_data = data[data[filter_column] > filter_value]
        st.session_state.filtered_data = filtered_data
        st.write(f"### Filtered Data (by `{filter_column} > {filter_value}`)")
        st.dataframe(filtered_data)

        # Show summary statistics in expander
        with st.expander("Show Summary Statistics"):
            st.write(filtered_data.describe())

    else:
        st.warning(f"Column `{filter_column}` not found in the dataset!")

    # Chart Visualization
    st.subheader(f"{chart_type} of `{filter_column}`")

    # Plot based on chart type
    if chart_type == "Line Chart":
        st.line_chart(st.session_state.filtered_data[filter_column] if filter_column else data)
    elif chart_type == "Bar Chart":
        st.bar_chart(st.session_state.filtered_data[filter_column] if filter_column else data)
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        ax.scatter(st.session_state.filtered_data.index, st.session_state.filtered_data[filter_column] if filter_column else data[filter_column], color=color)
        st.pyplot(fig)
    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        ax.hist(st.session_state.filtered_data[filter_column] if filter_column else data[filter_column], bins=20, color=color)
        st.pyplot(fig)
    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots()
        ax.pie(st.session_state.filtered_data[filter_column].value_counts() if filter_column else data[filter_column].value_counts(), labels=data[filter_column].unique(), autopct="%1.1f%%", colors=[color])
        st.pyplot(fig)

    # LaTeX Formula Example
    st.latex(r"\sum_{i=1}^{n} x_i = X")

    # Add a progress bar for simulation of processing
    st.subheader("Data Processing Progress")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)

    # Collaborative mode with user feedback
    if collaboration_mode:
        st.subheader("Live Collaboration Mode")
        feedback = st.text_area("Write your feedback or analysis notes here")

        if st.button("Submit Feedback"):
            st.write(f"Your Feedback: {feedback}")
            st.balloons()

        st.chat_input("Send a message to the team")
        with st.expander("Chat Messages"):
            # Simulate chat history
            st.chat_message("user1").write("User 1: Great insights!")
            st.chat_message("user2").write("User 2: Let’s dive deeper into the analysis.")

else:
    st.info("Please upload a CSV file to start.")

# Data Download
if not st.session_state.filtered_data.empty:
    st.subheader("Download Filtered Data")
    csv = st.session_state.filtered_data.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name="filtered_data.csv", mime="text/csv")

# Form for Feedback Submission
st.subheader("Feedback Form")
with st.form("feedback_form"):
    user_name = st.text_input("Your Name")
    feedback_message = st.text_area("Your Feedback")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Thank you, {user_name}, for your feedback!")
        st.write("Your feedback message:")
        st.write(feedback_message)

# Spinner Simulation for Long Tasks
st.subheader("Simulation of Long Running Task")
with st.spinner("Simulating long task..."):
    time.sleep(3)
st.success("Task completed!")

# Footer Section
st.markdown("---")
st.text("Collaborative Data Analytics Tool © 2024")
