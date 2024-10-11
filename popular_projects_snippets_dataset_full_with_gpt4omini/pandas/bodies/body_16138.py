# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# GH 25580
s = Series(range(9), dtype=dtype)
assert s.size == 9
