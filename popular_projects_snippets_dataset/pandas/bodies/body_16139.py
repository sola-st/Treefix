# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
s = Series([0, 1], name="abc")
assert s.attrs == {}
s.attrs["version"] = 1
result = s + 1
assert result.attrs == {"version": 1}
