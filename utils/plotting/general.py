from .bar_chart import plot_bar_chart

def plot(chart_type, **kwargs):

    if chart_type == "Bar Chart":

        chart_object = plot_bar_chart(**kwargs)
        return chart_object