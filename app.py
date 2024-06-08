import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader(label="File Upload",
                                 type="csv",
                                 accept_multiple_files=False,
                                 key="homepage-file-upload",
                                 label_visibility="visible")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    #st.dataframe(df)

with st.sidebar:
    st.markdown("# Add Visualization")
    if uploaded_file is None:
        st.error("Please upload a file before selecting a visualization")
    else:
        with st.form("add-visualization", border=False):
            visualization_type = st.selectbox(label="Visualization Type",
                                              options=("Bar Chart", ),
                                              index=None)

            submitted = st.form_submit_button()            