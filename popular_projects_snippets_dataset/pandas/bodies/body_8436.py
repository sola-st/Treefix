# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#24252 check that we get OutOfBoundsDatetime and not OverflowError
msg = "Out of bounds nanosecond timestamp"
start = Timestamp.max.floor("D").to_pydatetime()
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range(start, periods=2, freq="B")
