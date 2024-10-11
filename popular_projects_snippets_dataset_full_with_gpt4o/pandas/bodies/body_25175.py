# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
from pandas.plotting import plot_params

MPLPlot.__init__(self, data, **kwargs)
if self.stacked:
    self.data = self.data.fillna(value=0)
self.x_compat = plot_params["x_compat"]
if "x_compat" in self.kwds:
    self.x_compat = bool(self.kwds.pop("x_compat"))
