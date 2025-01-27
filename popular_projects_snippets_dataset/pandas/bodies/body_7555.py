# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py

# GH8083 test the base class for shift
msg = (
    "This method is only implemented for DatetimeIndex, PeriodIndex and "
    "TimedeltaIndex; Got type MultiIndex"
)
with pytest.raises(NotImplementedError, match=msg):
    idx.shift(1)
with pytest.raises(NotImplementedError, match=msg):
    idx.shift(1, 2)
