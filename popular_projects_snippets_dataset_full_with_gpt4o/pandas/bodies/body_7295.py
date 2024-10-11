# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta_range.py
# not enough params
msg = (
    "Of the four parameters: start, end, periods, and freq, "
    "exactly three must be specified"
)
with pytest.raises(ValueError, match=msg):
    timedelta_range(start="0 days")

with pytest.raises(ValueError, match=msg):
    timedelta_range(end="5 days")

with pytest.raises(ValueError, match=msg):
    timedelta_range(periods=2)

with pytest.raises(ValueError, match=msg):
    timedelta_range()

# too many params
with pytest.raises(ValueError, match=msg):
    timedelta_range(start="0 days", end="5 days", periods=10, freq="H")
