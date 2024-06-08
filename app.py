import streamlit as st
import pandas as pd
from utils.plotting.bar_chart import plot_bar_chart
from streamlit_echarts import st_pyecharts

PAGE_VISUALIZATIONS = []

uploaded_file = st.file_uploader(label="File Upload",
                                 type="csv",
                                 accept_multiple_files=False,
                                 key="homepage-file-upload",
                                 label_visibility="visible")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("")
    st.write("")
    #st.dataframe(df)

with st.sidebar:
    st.markdown("# Add Visualization")
    st.markdown("___")
    if uploaded_file is None:
        st.error("Please upload a file before selecting a visualization")
    else:
        with st.form("add-visualization", border=False):
            st.write("### Select Visualization Type")
            visualization_type = st.selectbox(label="Visualization Type",
                                              options=("Bar Chart", ),
                                              index=None,
                                              label_visibility="collapsed")
            
            st.write("### X-Axis Column")
            x_axis_column = st.selectbox(label="X-Axis Column",
                                         options=df.columns,
                                         index=None,
                                         label_visibility="collapsed")
            
            st.write("### Y-Axis Column")
            y_axis_column = st.selectbox(label="Y-Axis Column",
                                         options=df.columns,
                                         index=None,
                                         label_visibility="collapsed")
            

            submitted = st.form_submit_button()
            if submitted:
                if visualization_type == "Bar Chart":
                    PAGE_VISUALIZATIONS.append(plot_bar_chart(
                        x_axis_values = list(df[x_axis_column]),
                        y_axis_values = list(df[y_axis_column]),
                        x_label = x_axis_column,
                        y_label = y_axis_column,
                        title = "Top cloud providers 2018",
                        sub_title = "2017-2018 Revenue"
                    ))

st.markdown("# Visualizations")
if len(PAGE_VISUALIZATIONS) != 0:
    for visualization in PAGE_VISUALIZATIONS:
        st_pyecharts(visualization)
else:
    st.info("Currently no visualizations to display")