# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_asof.py
index = date_range("2010-01-01", periods=2, freq="m")
expected = Timestamp("2010-02-28")
result = index.asof("2010-02")
assert result == expected
assert not isinstance(result, Index)
