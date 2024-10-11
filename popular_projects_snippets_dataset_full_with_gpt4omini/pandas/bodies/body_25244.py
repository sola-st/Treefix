# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if return_type not in self._valid_return_types:
    raise ValueError("return_type must be {None, 'axes', 'dict', 'both'}")

self.return_type = return_type
# Do not call LinePlot.__init__ which may fill nan
MPLPlot.__init__(self, data, **kwargs)  # pylint: disable=non-parent-init-called
