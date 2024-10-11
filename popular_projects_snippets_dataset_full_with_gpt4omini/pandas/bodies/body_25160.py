# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
MPLPlot.__init__(self, data, **kwargs)
if x is None or y is None:
    raise ValueError(self._kind + " requires an x and y column")
if is_integer(x) and not self.data.columns._holds_integer():
    x = self.data.columns[x]
if is_integer(y) and not self.data.columns._holds_integer():
    y = self.data.columns[y]

# Scatter plot allows to plot objects data
if self._kind == "hexbin":
    if len(self.data[x]._get_numeric_data()) == 0:
        raise ValueError(self._kind + " requires x column to be numeric")
    if len(self.data[y]._get_numeric_data()) == 0:
        raise ValueError(self._kind + " requires y column to be numeric")

self.x = x
self.y = y
