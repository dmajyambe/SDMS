import pandas as pd
import streamlit as st

data = None
# @st.cache_data(experimental_allow_widgets=True)
def read_data():
    global data
    uploaded_file = st.sidebar.file_uploader("Upload school dataset", type=["xlsx"])
    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
    if data is None:
        data = pd.read_excel("2022_2023 shaded school dataset 29.11.2023.xlsx")
    return data
