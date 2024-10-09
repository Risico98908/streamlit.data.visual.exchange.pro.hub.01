```python
import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Interactive Dashboard Example")

# Header and subheader
st.header("User Input and Data Display")
st.subheader("Upload your dataset")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display data
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    # Column selection using multiselect
    selected_columns = st.multiselect("Select columns to display", data.columns)
    if selected_columns:
        st.dataframe(data[selected_columns])

    # Show Data Statistics
    st.write("Summary Statistics:")
    st.write(data.describe())

    # Add divider
    st.divider()

    # Checkbox and radio button interaction
    if st.checkbox("Show additional info"):
        selected_chart = st.radio("Choose chart type", ["Bar", "Line", "Scatter"])

        if selected_chart == "Bar":
            st.bar_chart(data[selected_columns])
        elif selected_chart == "Line":
            st.line_chart(data[selected_columns])
        elif selected_chart == "Scatter":
            st.scatter_chart(data[selected_columns])

    # Code snippet for clarity
    st.code("""
    # Sample code for reading CSV file:
    df = pd.read_csv('your_file.csv')
    """)

    # Success message and metric display
    st.success("Data uploaded successfully!")
    st.metric(label="Max Value", value=f"{data[selected_columns].max().max():.2f}")

    # Button action for performing analysis
    if st.button("Run Analysis"):
        st.spinner("Running analysis...")
        st.write("Analysis complete!")

# Sidebar inputs and layout
st.sidebar.header("Options")
slider_value = st.sidebar.slider("Select a range", 0, 100, 50)
st.sidebar.text(f"Slider value: {slider_value}")

# Balloon celebration
if st.sidebar.button("Celebrate"):
    st.balloons()

# Footer text
st.text("Interactive Streamlit Dashboard © 2024")
```

### Explanation:

1. **Data Interaction**: Users can upload CSVs, select specific columns to display, and filter data using widgets like multiselect, sliders, and radio buttons.
2. **Visualization Options**: Bar, line, and scatter charts are dynamically rendered based on the selected columns and user input.
3. **Additional Features**: The app includes success messages, metrics, code snippets, and a fun feature with balloons for celebratory actions.
