import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar


def summarize_data(df, x_column, y_column, agg_function="sum"):
    """
    ID  Company     Revenue
    1   Google      4.0
    2   Microsoft   12.1
    If dataframe provided was in the above format while plotting a bar chart we can just extract the values from the columns.

    ID  Company     Revenue     -> summarize_data ->    ID  Company     Revenue
    1   Google      4.0                                 1   Google      4.0
    2   Microsoft   12.1                                2   Microsoft   19.3
    3   Google      7.2
    In such cases the y_column, in general we would expect the y_column to be aggregated. Hence we have summarize the dataframe
    """

    summarized_df = df.groupby(x_column).agg({y_column : agg_function})
    summarized_df.reset_index(drop=False, inplace=True)
    return summarized_df

def summarize_data_by_extra_variable(df, x_column, y_column, extra_variable, agg_function="sum"):
    extra_col_unique_vals = df[extra_variable].unique()
    df_subsets = [df[df[extra_variable] == item] for item in extra_col_unique_vals]
    return df_subsets

def create_bar_chart(x_axis_values,
                   y_axis_values,
                   x_label,
                   y_label,
                   title,
                   sub_title):
    
    b = (
        Bar()
        .add_xaxis(x_axis_values)
        .add_yaxis(y_label, y_axis_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title, subtitle=sub_title
            ),
            xaxis_opts=opts.AxisOpts(name=x_label),
            yaxis_opts=opts.AxisOpts(name=y_label)
        )
    )

    return b

def create_bar_chart_by_color(x_axis_values,
                              y_axis_values_by_subset,
                              x_label,
                              y_label,
                              title,
                              sub_title,
                              unique_color_col_vals):
    b = (
        Bar()
        .add_xaxis(x_axis_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title, subtitle=sub_title
            ),
            xaxis_opts=opts.AxisOpts(name=x_label),
            yaxis_opts=opts.AxisOpts(name=y_label)
        )
    )

    for color_col_label, y_axis_values in zip(unique_color_col_vals, y_axis_values_by_subset):
        b = b.add_yaxis(str(color_col_label), y_axis_values, stack="stack1")

    return b


def plot_bar_chart(df, x_column, y_column, x_label, y_label, title, sub_title, color):

    if x_label == "": x_label = x_column
    if y_label == "": y_label = y_column

    if (df[y_column].dtype == float) or (df[y_column].dtype == int):

        if color is None:

            summarized_data = summarize_data(df, x_column, y_column)
            x_axis_values, y_axis_values = summarized_data[x_column].to_list(), summarized_data[y_column].to_list()
            bar_chart = create_bar_chart(x_axis_values, y_axis_values, x_label, y_label, title, sub_title)

            return bar_chart
        
        else:
            unique_color_col_vals = df[color].unique()
            df_subsets = [df[df[color] == item] for item in unique_color_col_vals]
            df_subsets = [summarize_data(item, x_column, y_column) for item in df_subsets]
            x_axis_values = df_subsets[0].index.to_list()
            y_axis_values_by_subset = [item[y_column].to_list() for item in df_subsets]
            bar_chart = create_bar_chart_by_color(x_axis_values, y_axis_values_by_subset, x_label, y_label, title, sub_title, unique_color_col_vals)

            return bar_chart
    
    else:
        error_message = f"Bar Chart Y-Axis expects column of type `float` or `int`. But found `{df[y_column].dtype}`"
        plotting_error(error_message)

        return None
    
@st.experimental_dialog("Plotting Error!")
def plotting_error(error_message):
    st.write(error_message)