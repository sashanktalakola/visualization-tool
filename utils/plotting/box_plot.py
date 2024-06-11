import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Boxplot


def create_box_plot(
        x_axis_values,
        y_axis_values,
        x_label,
        y_label,
        title,
        sub_title):
    
    c = Boxplot()
    c.add_xaxis(x_axis_values)
    c.add_yaxis(y_label, y_axis_values)
    c.set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=sub_title),
            xaxis_opts=opts.AxisOpts(name=x_label)
    )

    return c

def plot_box_plot(df, x_column, y_column, x_label, y_label, title, sub_title):
    if x_label == "": x_label = x_column
    if y_label == "": y_label = y_column

    if (df[y_column].dtype == float) or (df[y_column].dtype == int):
        
        x_axis_values = df[x_column].unique().tolist()
        y_axis_values = []
        for x_axis_value in x_axis_values:
            y_axis_value = df[df[x_column] == x_axis_value][y_column].to_list()
            y_axis_values.append(y_axis_value)
        
        box_plot = create_box_plot(x_axis_values, y_axis_values, x_label, y_label, title, sub_title)
        return box_plot

    else:
        error_message = f"Box Plot Y-Axis expects column of type `float` or `int`. But found `{df[y_column].dtype}`"
        plotting_error(error_message)

        return None
    
@st.experimental_dialog("Plotting Error!")
def plotting_error(error_message):
    st.write(error_message)