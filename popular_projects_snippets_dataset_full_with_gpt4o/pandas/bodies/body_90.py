# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# https://github.com/pandas-dev/pandas/issues/17648
# Checks that np.nan key is appropriately mapped
s = Series([1, 2, np.nan])
expected = Series(["a", "b", "c"])
result = s.map({1: "a", 2: "b", np.nan: "c"})
tm.assert_series_equal(result, expected)
