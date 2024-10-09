import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Dynamic Data Exploration")

# Sidebar configuration
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Radio button for chart type
chart_type = st.sidebar.radio("Chart Type", ['Line', 'Bar', 'Scatter'])

# Selectbox for column filtering
st.sidebar.subheader("Select Filters")
selected_column = st.sidebar.selectbox("Choose column for analysis", [])

# Slider for numeric filtering
filter_value = st.sidebar.slider("Filter data by value", 0, 100, 50)

if uploaded_file is not None:
    # Read uploaded CSV
    data = pd.read_csv(uploaded_file)

    # Display data and filtered data
    st.subheader("Uploaded Data")
    st.dataframe(data)

    st.subheader(f"Filtered {selected_column} Data")
    filtered_data = data[data[selected_column] > filter_value]
    st.table(filtered_data)

    # Display Chart based on user choice
    st.subheader("Data Visualization")
    if chart_type == 'Line':
        st.line_chart(filtered_data[selected_column])
    elif chart_type == 'Bar':
        st.bar_chart(filtered_data[selected_column])
    else:
        st.scatter_chart(filtered_data[selected_column])

    # Expander for summary statistics
    with st.expander("Show Summary Statistics"):
        st.write(filtered_data.describe())

    # Metrics and progress
    st.metric("Max Value", filtered_data[selected_column].max())
    st.progress(int(filtered_data[selected_column].max()))

    # Display a LaTeX formula
    st.latex(r"a^2 + b^2 = c^2")

    # Button with success message
    if st.button("Analyze"):
        st.success("Analysis Complete!")

    # Balloons for fun!
    st.balloons()

# Footer Text
st.text("Data Exploration App © 2024")
