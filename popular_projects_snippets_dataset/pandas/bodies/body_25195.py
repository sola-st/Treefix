# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# we have to treat a series differently than a
# 1-column DataFrame w.r.t. color handling
self._is_series = isinstance(data, ABCSeries)
self.bar_width = kwargs.pop("width", 0.5)
pos = kwargs.pop("position", 0.5)
kwargs.setdefault("align", "center")
self.tick_pos = np.arange(len(data))

self.bottom = kwargs.pop("bottom", 0)
self.left = kwargs.pop("left", 0)

self.log = kwargs.pop("log", False)
MPLPlot.__init__(self, data, **kwargs)

if self.stacked or self.subplots:
    self.tickoffset = self.bar_width * pos
    if kwargs["align"] == "edge":
        self.lim_offset = self.bar_width / 2
    else:
        self.lim_offset = 0
else:
    if kwargs["align"] == "edge":
        w = self.bar_width / self.nseries
        self.tickoffset = self.bar_width * (pos - 0.5) + w * 0.5
        self.lim_offset = w * 0.5
    else:
        self.tickoffset = self.bar_width * pos
        self.lim_offset = 0

self.ax_pos = self.tick_pos - self.tickoffset
