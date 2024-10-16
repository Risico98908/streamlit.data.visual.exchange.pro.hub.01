#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# App Title and Header
st.title("DataSphere: Advanced Analytics & Collaboration Platform")
st.header("Explore, Visualize, Collaborate, and Analyze Data Efficiently")

# Sidebar Configuration: File Upload & Settings
st.sidebar.header("Data Upload and Settings")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Sidebar for visualization options
chart_type = st.sidebar.radio("Choose Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Area Chart"])
filter_column = st.sidebar.text_input("Filter by Column Name")
value_filter = st.sidebar.slider("Filter Values Greater Than", 0, 100, 25)
chart_color = st.sidebar.color_picker("Select Chart Color", "#FF5733")

# Collaborative features in the sidebar
collaboration_mode = st.sidebar.checkbox("Enable Collaboration Mode")
feedback_mode = st.sidebar.checkbox("Enable Feedback")

# User login simulation
st.sidebar.subheader("Login")
username = st.sidebar.text_input("Username", "")
password = st.sidebar.text_input("Password", type="password")
login = st.sidebar.button("Login")

if login:
    if username == "admin" and password == "password":
        st.sidebar.success("Logged in as Admin!")
    else:
        st.sidebar.error("Invalid username or password")

# Main app section: Data Handling and Visualization
st.header("Dataset Overview and Analytics")

# If file uploaded
if uploaded_file:
    # Reading the data and displaying the first few rows
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview")
    st.dataframe(data.head(10))

    # Filtering data based on user input
    if filter_column and filter_column in data.columns:
        filtered_data = data[data[filter_column] > value_filter]
        st.write(f"Filtered Data (where `{filter_column}` > {value_filter})")
        st.dataframe(filtered_data)

        # Data Summary Statistics
        with st.expander("Show Summary Statistics"):
            st.write(filtered_data.describe())

        # Chart Visualization
        st.subheader(f"{chart_type} of `{filter_column}`")
        if chart_type == "Line Chart":
            st.line_chart(filtered_data[filter_column])
        elif chart_type == "Bar Chart":
            st.bar_chart(filtered_data[filter_column])
        elif chart_type == "Scatter Plot":
            fig, ax = plt.subplots()
            ax.scatter(filtered_data.index, filtered_data[filter_column], color=chart_color)
            st.pyplot(fig)
        elif chart_type == "Pie Chart":
            pie_data = filtered_data[filter_column].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=[chart_color])
            st.pyplot(fig)
        elif chart_type == "Area Chart":
            st.area_chart(filtered_data[filter_column])

        # Download filtered data
        st.subheader("Download Filtered Data")
        csv = filtered_data.to_csv(index=False)
        st.download_button("Download CSV", data=csv, file_name="filtered_data.csv", mime="text/csv")

    else:
        st.warning(f"Column `{filter_column}` not found in the dataset!")

# Simulating progress for large dataset analysis
st.header("Processing Large Datasets")
with st.spinner("Analyzing your data..."):
    for i in range(100):
        time.sleep(0.02)
        st.progress(i + 1)
st.success("Data analysis completed!")

# Collaborative Mode: Chat and Feedback
if collaboration_mode:
    st.header("Collaborative Mode: Live Chat")
    chat_message = st.chat_input("Send a message to your team")
    if chat_message:
        st.write(f"You: {chat_message}")
    with st.expander("Chat History"):
        st.chat_message("User1").write("User1: Let's focus on the outliers.")
        st.chat_message("User2").write("User2: Agreed, let's clean the data and rerun the analysis.")

# Feedback Mode
if feedback_mode:
    st.header("Submit Feedback")
    with st.form("feedback_form"):
        user_name = st.text_input("Your Name")
        feedback_message = st.text_area("Your Feedback")
        submitted = st.form_submit_button("Submit Feedback")
        if submitted:
            st.write(f"Thank you, {user_name}, for your feedback!")
            st.write(f"Feedback: {feedback_message}")

# Key Metrics Display
st.header("Key Metrics")
if uploaded_file and filter_column:
    st.metric("Max Value", filtered_data[filter_column].max())
    st.metric("Min Value", filtered_data[filter_column].min())
    st.metric("Mean Value", round(filtered_data[filter_column].mean(), 2))

# LaTeX Formula for advanced analysis
st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

# Footer Section
st.markdown("---")
st.text("DataSphere © 2024 | Powered by Streamlit")
