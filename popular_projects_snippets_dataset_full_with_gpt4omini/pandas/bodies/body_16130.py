# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
s = Series([1, 2, np.nan])
tm.assert_series_equal(s.dropna(axis="rows"), s.dropna(axis="index"))
assert s.dropna().sum("rows") == 3
assert s._get_axis_number("rows") == 0
assert s._get_axis_name("rows") == "index"
