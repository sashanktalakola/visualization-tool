import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Boxplot


def process_values(df, x_column, y_column):
    x_axis_values = df[x_column].unique().tolist()
    y_axis_values = []
    for x_axis_value in x_axis_values:
        y_axis_value = df[df[x_column] == x_axis_value][y_column].to_list()
        y_axis_values.append(y_axis_value)

    return x_axis_values, y_axis_values


def create_box_plot(
        x_axis_values,
        y_axis_values,
        x_label,
        y_label,
        title,
        sub_title):
    
    c = Boxplot()
    c.add_xaxis(x_axis_values)
    c.add_yaxis(y_label, c.prepare_data(y_axis_values))
    c.set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=sub_title),
            xaxis_opts=opts.AxisOpts(name=x_label)
    )

    return c

def create_box_plot_by_color(
        x_axis_values,
        y_axis_values,
        x_label,
        y_label,
        title,
        sub_title,
        unique_color_col_vals):
    
    c = Boxplot()
    c.add_xaxis(x_axis_values)
    c.set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=sub_title),
            xaxis_opts=opts.AxisOpts(name=x_label),
            yaxis_opts=opts.AxisOpts(name=y_label)
    )

    for label, y_axis_value in zip(unique_color_col_vals, y_axis_values):
        c = c.add_yaxis(label, c.prepare_data(y_axis_value))

    return c

def plot_box_plot(df, x_column, y_column, x_label, y_label, title, sub_title, color):
    if x_label == "": x_label = x_column
    if y_label == "": y_label = y_column

    if (df[y_column].dtype == float) or (df[y_column].dtype == int):

        if color is None:
        
            df = df.dropna(subset=[x_column, y_column])
            x_axis_values, y_axis_values = process_values(df, x_column, y_column)
            box_plot = create_box_plot(x_axis_values, y_axis_values, x_label, y_label, title, sub_title)
            
            return box_plot
        
        else:

            df = df.dropna(subset=[x_column, y_column, color])
            unique_color_col_vals = df[color].unique()
            df_subsets = [df[df[color] == item] for item in unique_color_col_vals]

            x_axis_values = df[x_column].unique().tolist()
            y_axis_values = [process_values(df_subset, x_column, y_column) for df_subset in df_subsets]
            box_plot = create_box_plot_by_color(x_axis_values, y_axis_values, x_label, y_label, title, sub_title, unique_color_col_vals)

            return box_plot


    else:
        error_message = f"Box Plot Y-Axis expects column of type `float` or `int`. But found `{df[y_column].dtype}`"
        plotting_error(error_message)

        return None
    
@st.experimental_dialog("Plotting Error!")
def plotting_error(error_message):
    st.write(error_message)