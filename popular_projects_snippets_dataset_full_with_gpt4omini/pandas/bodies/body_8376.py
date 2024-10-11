# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#???
freq = Timedelta(1)

with pytest.raises(OutOfBoundsDatetime, match="Cannot generate range with"):
    date_range(end=Timestamp.min, periods=2, freq=freq)
