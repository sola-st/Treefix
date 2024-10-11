# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
# Do not call LinePlot.__init__ which may fill nan
MPLPlot.__init__(self, data, **kwargs)  # pylint: disable=non-parent-init-called
self.bw_method = bw_method
self.ind = ind
