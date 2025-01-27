# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period_range.py
# not enough params
msg = (
    "Of the three parameters: start, end, and periods, "
    "exactly two must be specified"
)
with pytest.raises(ValueError, match=msg):
    period_range(start="2017Q1")

with pytest.raises(ValueError, match=msg):
    period_range(end="2017Q1")

with pytest.raises(ValueError, match=msg):
    period_range(periods=5)

with pytest.raises(ValueError, match=msg):
    period_range()

# too many params
with pytest.raises(ValueError, match=msg):
    period_range(start="2017Q1", end="2018Q1", periods=8, freq="Q")

# start/end NaT
msg = "start and end must not be NaT"
with pytest.raises(ValueError, match=msg):
    period_range(start=NaT, end="2018Q1")

with pytest.raises(ValueError, match=msg):
    period_range(start="2017Q1", end=NaT)

# invalid periods param
msg = "periods must be a number, got foo"
with pytest.raises(TypeError, match=msg):
    period_range(start="2017Q1", periods="foo")
