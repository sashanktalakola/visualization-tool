from pyecharts import options as opts
from pyecharts.charts import Bar

def plot_bar_chart(x_axis_values,
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