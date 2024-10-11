# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#24255
# case with start later than 1970-01-01, overflow int64 but not uint64
msg = "Cannot generate range with"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range(start="1970-02-01", periods=106752 * 24, freq="H")

# case with end before 1970-01-01, overflow int64 but not uint64
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range(end="1969-11-14", periods=106752 * 24, freq="H")
