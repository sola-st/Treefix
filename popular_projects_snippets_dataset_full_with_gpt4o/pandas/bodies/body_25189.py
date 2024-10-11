# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
kwargs.setdefault("stacked", True)
data = data.fillna(value=0)
LinePlot.__init__(self, data, **kwargs)

if not self.stacked:
    # use smaller alpha to distinguish overlap
    self.kwds.setdefault("alpha", 0.5)

if self.logy or self.loglog:
    raise ValueError("Log-y scales are not supported in area plot")
