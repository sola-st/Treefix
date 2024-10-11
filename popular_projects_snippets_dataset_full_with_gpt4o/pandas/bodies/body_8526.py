# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/16515
idx = DatetimeIndex(["2017", "2017"])
result = idx._maybe_cast_slice_bound("2017-01-01", "left")
expected = Timestamp("2017-01-01")
assert result == expected
