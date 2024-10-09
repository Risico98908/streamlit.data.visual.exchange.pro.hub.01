```python
import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Random Streamlit Function Showcase")

# Header and Subheader
st.header("Data Input and Display")
st.subheader("Upload and Filter Your Dataset")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Select Columns
    selected_columns = st.multiselect("Select columns to display", data.columns)

    if selected_columns:
        st.dataframe(data[selected_columns])

    # Display data summary
    st.write("Data Summary")
    st.write(data.describe())

    # Divider
    st.divider()

    # Checkbox for additional information
    show_info = st.checkbox("Show More Information")

    if show_info:
        st.info("Detailed statistics and analysis can be added here.")

    # Line Chart
    if 'Value' in data.columns:
        st.line_chart(data['Value'])

    # Show code sample
    st.code('''df = pd.read_csv('your_file.csv')''')

    # Use of metrics
    st.metric("Mean Value", f"{data['Value'].mean():.2f}")

    # Progress bar
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    # Date input
    selected_date = st.date_input("Select a date")

    # Button to simulate analysis
    if st.button("Run Analysis"):
        st.success("Analysis Completed!")

    # Add balloons
    st.balloons()

# Sidebar with slider and radio buttons
st.sidebar.header("Control Panel")
st.sidebar.slider("Select a range", 0, 100, 50)
chart_type = st.sidebar.radio("Choose Chart Type", ["Line", "Bar", "Area"])

# Example charts in the sidebar
st.sidebar.text("Example Charts")
st.sidebar.line_chart(np.random.randn(100, 2))

# Footer Text
st.text("Streamlit Function Showcase © 2024")
```

### Explanation:

1. **User Interaction**: Users upload a CSV, select columns, and apply filters. The app dynamically displays charts, metrics, and summary.
2. **Widgets and Visualization**: Charts, metrics, checkboxes, and progress bars provide interactive data visualization and insights to users.
3. **Sidebar Controls**: The sidebar contains sliders, radio buttons, and charts to customize the app’s behavior and enhance user engagement.
