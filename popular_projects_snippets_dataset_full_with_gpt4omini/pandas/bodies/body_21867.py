# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
self.obj = obj
self.on = on
self.closed = closed
self.step = step
self.window = window
self.min_periods = min_periods
self.center = center
self.win_type = win_type
self.axis = obj._get_axis_number(axis) if axis is not None else None
self.method = method
self._win_freq_i8: int | None = None
if self.on is None:
    if self.axis == 0:
        self._on = self.obj.index
    else:
        # i.e. self.axis == 1
        self._on = self.obj.columns
elif isinstance(self.on, Index):
    self._on = self.on
elif isinstance(self.obj, ABCDataFrame) and self.on in self.obj.columns:
    self._on = Index(self.obj[self.on])
else:
    raise ValueError(
        f"invalid on specified as {self.on}, "
        "must be a column (of DataFrame), an Index or None"
    )

self._selection = selection
self._validate()
