# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH 21881
timestamp = Timestamp(1412526600000000000)
series = Series([timestamp], index=["timestamp"], dtype=object)
expected = series["timestamp"]

series = Series([], dtype=object)
series["anything"] = 300.0
series["timestamp"] = timestamp
result = series["timestamp"]
assert result == expected
