# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#14187
msg = "Cannot generate range"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range("2016-01-01", periods=100000, freq="D")
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range(end="1763-10-12", periods=100000, freq="D")
