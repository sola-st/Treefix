# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
super().__init__(
    obj=obj,
    min_periods=1 if min_periods is None else max(int(min_periods), 1),
    on=None,
    center=False,
    closed=None,
    method=method,
    axis=axis,
    selection=selection,
)
self.com = com
self.span = span
self.halflife = halflife
self.alpha = alpha
self.adjust = adjust
self.ignore_na = ignore_na
self.times = times
if self.times is not None:
    if not self.adjust:
        raise NotImplementedError("times is not supported with adjust=False.")
    if not is_datetime64_ns_dtype(self.times):
        raise ValueError("times must be datetime64[ns] dtype.")
    if len(self.times) != len(obj):
        raise ValueError("times must be the same length as the object.")
    if not isinstance(self.halflife, (str, datetime.timedelta, np.timedelta64)):
        raise ValueError("halflife must be a timedelta convertible object")
    if isna(self.times).any():
        raise ValueError("Cannot convert NaT values to integer")
    self._deltas = _calculate_deltas(self.times, self.halflife)
    # Halflife is no longer applicable when calculating COM
    # But allow COM to still be calculated if the user passes other decay args
    if common.count_not_none(self.com, self.span, self.alpha) > 0:
        self._com = get_center_of_mass(self.com, self.span, None, self.alpha)
    else:
        self._com = 1.0
else:
    if self.halflife is not None and isinstance(
        self.halflife, (str, datetime.timedelta, np.timedelta64)
    ):
        raise ValueError(
            "halflife can only be a timedelta convertible argument if "
            "times is not None."
        )
    # Without times, points are equally spaced
    self._deltas = np.ones(
        max(self.obj.shape[self.axis] - 1, 0), dtype=np.float64
    )
    self._com = get_center_of_mass(
        # error: Argument 3 to "get_center_of_mass" has incompatible type
        # "Union[float, Any, None, timedelta64, signedinteger[_64Bit]]";
        # expected "Optional[float]"
        self.com,
        self.span,
        self.halflife,  # type: ignore[arg-type]
        self.alpha,
    )
