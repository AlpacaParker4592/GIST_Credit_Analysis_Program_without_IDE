import _plotly_utils.basevalidators


class LinewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="linewidth", parent_name="layout.xaxis", **kwargs):
        super(LinewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "ticks+layoutstyle"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
