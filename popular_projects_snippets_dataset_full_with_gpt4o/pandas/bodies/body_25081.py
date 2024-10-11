# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
self.bins = bins  # use mpl default
self.bottom = bottom
self.xlabel = kwargs.get("xlabel")
self.ylabel = kwargs.get("ylabel")
# Do not call LinePlot.__init__ which may fill nan
MPLPlot.__init__(self, data, **kwargs)  # pylint: disable=non-parent-init-called
