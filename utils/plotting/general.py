import streamlit as st
from .bar_chart import plot_bar_chart
from .box_plot import plot_box_plot


def plot(chart_type, **kwargs):

    if chart_type == "Bar Chart":

        chart_object = plot_bar_chart(**kwargs)
        return chart_object
    
    elif chart_type == "Box Plot":

        chart_object = plot_box_plot(**kwargs)
        return chart_object
    
def display_plot_options_form(chart_type, df):
    if chart_type == "Bar Chart":

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
        
        st.write("### Title &nbsp;`Optional`")
        title = st.text_input(label="Title",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### Sub-Title &nbsp;`Optional`")
        sub_title = st.text_input(label="Sub-Title",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### X-Axis Label &nbsp;`Optional`")
        x_axis_label = st.text_input(label="x-label",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### Y-Axis Label &nbsp;`Optional`")
        y_axis_label = st.text_input(label="y-label",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### Color &nbsp;`Optional`")
        color = st.selectbox(label="Color",
                            options=df.columns,
                            index=None,
                            label_visibility="collapsed")

        plot_options = {
            "x_column":x_axis_column,
            "y_column":y_axis_column,
            "x_label":x_axis_label,
            "y_label":y_axis_label,
            "title":title,
            "sub_title":sub_title,
            "color": color
        }
        return plot_options
    
    elif chart_type == "Box Plot":
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
        
        st.write("### Title &nbsp;`Optional`")
        title = st.text_input(label="Title",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### Sub-Title &nbsp;`Optional`")
        sub_title = st.text_input(label="Sub-Title",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### X-Axis Label &nbsp;`Optional`")
        x_axis_label = st.text_input(label="x-label",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### Y-Axis Label &nbsp;`Optional`")
        y_axis_label = st.text_input(label="y-label",
                                value="",
                                label_visibility="collapsed")
        
        st.write("### Color &nbsp;`Optional`")
        color = st.selectbox(label="Color",
                            options=df.columns,
                            index=None,
                            label_visibility="collapsed")
        
        plot_options = {
            "x_column":x_axis_column,
            "y_column":y_axis_column,
            "x_label":x_axis_label,
            "y_label":y_axis_label,
            "title":title,
            "sub_title":sub_title,
            "color": color
        }
        return plot_options