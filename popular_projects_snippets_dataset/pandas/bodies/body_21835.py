# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
if times is not None:
    raise NotImplementedError(
        "times is not implemented with online operations."
    )
super().__init__(
    obj=obj,
    com=com,
    span=span,
    halflife=halflife,
    alpha=alpha,
    min_periods=min_periods,
    adjust=adjust,
    ignore_na=ignore_na,
    axis=axis,
    times=times,
    selection=selection,
)
self._mean = EWMMeanState(
    self._com, self.adjust, self.ignore_na, self.axis, obj.shape
)
if maybe_use_numba(engine):
    self.engine = engine
    self.engine_kwargs = engine_kwargs
else:
    raise ValueError("'numba' is the only supported engine")
