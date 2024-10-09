import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Interactive Data Insights")

# Header and subheader
st.header("Data Upload and Overview")
st.subheader("Upload your CSV dataset")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display data
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    # Column selection using selectbox
    selected_column = st.selectbox("Select column to visualize", data.columns)

    # Line chart for selected column
    st.line_chart(data[selected_column])

    # Show summary statistics
    st.subheader("Data Summary")
    st.table(data.describe())

    # Divider
    st.divider()

    # Checkbox and color picker interaction
    if st.checkbox("Show additional info"):
        selected_color = st.color_picker("Pick a color for chart")

        st.markdown(f"### You selected: `{selected_color}`")
        st.area_chart(data[selected_column])

    # Display success and info messages
    st.success("Data successfully uploaded and visualized!")
    st.info(f"Column '{selected_column}' visualized above.")

    # Button to simulate analysis
    if st.button("Run Data Analysis"):
        with st.spinner("Analyzing..."):
            st.write("Analysis completed!")
    
    # LaTeX formula display
    st.latex(r"\sum_{i=1}^{n} x_i = X")

    # Expander to show more
    with st.expander("Click to expand"):
        st.write("More data can be shown here!")

# Sidebar with slider and radio buttons
st.sidebar.header("Controls")
filter_value = st.sidebar.slider("Select minimum value", 0, 100, 10)
st.sidebar.radio("Chart Style", ["Line", "Bar"])

# Footer Text
st.text("Data Insights Dashboard © 2024")
