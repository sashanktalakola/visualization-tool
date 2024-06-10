from pyecharts import options as opts
from pyecharts.charts import Bar


def summarize_data(df, x_column, y_column, agg_function="sum"):
    """
    ID  Company     Revenue
    1   Google      4.0
    2   Microsoft   12.1
    If dataframe provided was in the above format while plotting a bar chart we can just extract the values from the columns.

    ID  Company     Revenue
    1   Google      4.0
    2   Microsoft   12.1
    3   Google      7.2
    In such cases the y_column, in general we would expect the y_column to be aggregated. Hence we have summarize the dataframe
    
    """

    summarized_df = df.groupby(x_column).agg({y_column : agg_function})
    return summarized_df.index.to_list(), summarized_df[y_column].to_list()

def create_bar_chart(x_axis_values,
                   y_axis_values,
                   x_label,
                   y_label,
                   title,
                   sub_title,
                   ):
    
    b = (
        Bar()
        .add_xaxis(x_axis_values)
        .add_yaxis(y_label, y_axis_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title, subtitle=sub_title
            ),
        )
    )

    return b

def plot_bar_chart(df, x_column, y_column, x_label, y_label, title, sub_title):

    if x_label == "": x_label = x_column
    if y_label == "": y_label = y_column

    x_axis_values, y_axis_values = summarize_data(df, x_column, y_column)
    bar_chart = create_bar_chart(x_axis_values, y_axis_values, x_label, y_label, title, sub_title)

    return bar_chart