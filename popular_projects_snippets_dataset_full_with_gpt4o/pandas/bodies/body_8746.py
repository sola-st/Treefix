# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#19643 previously overflowed silently
pi = pd.period_range("1500", freq="Y", periods=3)
msg = "Out of bounds nanosecond timestamp: 1500-01-01 00:00:00"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    pi.to_timestamp()

with pytest.raises(OutOfBoundsDatetime, match=msg):
    pi._data.to_timestamp()
