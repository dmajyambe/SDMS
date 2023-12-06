import pandas as pd
import streamlit as st

@st.cache_data(experimental_allow_widgets=True)
# Function to read the data without caching
def read_data():
    uploaded_file = st.file_uploader("Upload school dataset", type=["xlsx"], key="file_uploader_key")
    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
        return data
    else:
        st.warning("Please upload a valid Excel file.")
        st.stop()



