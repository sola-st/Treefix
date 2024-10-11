# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
data = data.fillna(value=0)
if (data < 0).any().any():
    raise ValueError(f"{self._kind} plot doesn't allow negative values")
MPLPlot.__init__(self, data, kind=kind, **kwargs)
