# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
s = pd.Series(["a", "b", None], dtype=dtype)

result = s.isin(["a", "c"])
expected = pd.Series([True, False, False])
tm.assert_series_equal(result, expected)

result = s.isin(["a", pd.NA])
expected = pd.Series([True, False, True])
tm.assert_series_equal(result, expected)

result = s.isin([])
expected = pd.Series([False, False, False])
tm.assert_series_equal(result, expected)

result = s.isin(["a", fixed_now_ts])
expected = pd.Series([True, False, False])
tm.assert_series_equal(result, expected)
