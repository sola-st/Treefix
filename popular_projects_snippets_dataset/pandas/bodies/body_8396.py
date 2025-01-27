# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH #1095
msg = (
    "Of the four parameters: start, end, periods, and "
    "freq, exactly three must be specified"
)

with pytest.raises(ValueError, match=msg):
    date_range(start="1/1/2000")

with pytest.raises(ValueError, match=msg):
    date_range(end="1/1/2000")

with pytest.raises(ValueError, match=msg):
    date_range(periods=10)

with pytest.raises(ValueError, match=msg):
    date_range(start="1/1/2000", freq="H")

with pytest.raises(ValueError, match=msg):
    date_range(end="1/1/2000", freq="H")

with pytest.raises(ValueError, match=msg):
    date_range(periods=10, freq="H")

with pytest.raises(ValueError, match=msg):
    date_range()
