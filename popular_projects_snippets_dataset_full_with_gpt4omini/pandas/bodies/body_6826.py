# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# filler input data to be used when supplying invalid kwargs
filler = self.get_kwargs_from_breaks(range(10))

# invalid closed
msg = "closed must be one of 'right', 'left', 'both', 'neither'"
with pytest.raises(ValueError, match=msg):
    constructor(closed="invalid", **filler)

# unsupported dtype
msg = "dtype must be an IntervalDtype, got int64"
with pytest.raises(TypeError, match=msg):
    constructor(dtype="int64", **filler)

# invalid dtype
msg = "data type [\"']invalid[\"'] not understood"
with pytest.raises(TypeError, match=msg):
    constructor(dtype="invalid", **filler)

# no point in nesting periods in an IntervalIndex
periods = period_range("2000-01-01", periods=10)
periods_kwargs = self.get_kwargs_from_breaks(periods)
msg = "Period dtypes are not supported, use a PeriodIndex instead"
with pytest.raises(ValueError, match=msg):
    constructor(**periods_kwargs)

# decreasing values
decreasing_kwargs = self.get_kwargs_from_breaks(range(10, -1, -1))
msg = "left side of interval must be <= right side"
with pytest.raises(ValueError, match=msg):
    constructor(**decreasing_kwargs)
