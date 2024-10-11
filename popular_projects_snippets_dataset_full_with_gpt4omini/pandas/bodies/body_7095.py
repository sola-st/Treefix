# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py

# GH8083 test the base class for shift
idx = simple_index
msg = (
    f"This method is only implemented for DatetimeIndex, PeriodIndex and "
    f"TimedeltaIndex; Got type {type(idx).__name__}"
)
with pytest.raises(NotImplementedError, match=msg):
    idx.shift(1)
with pytest.raises(NotImplementedError, match=msg):
    idx.shift(1, 2)
