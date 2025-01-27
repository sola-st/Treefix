# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# gh 22158

# na for category
values = Series(["a", "b", "c", "a", np.nan], dtype="category")
result = values.str.contains("a", na=True)
expected = Series([True, False, False, True, True])
tm.assert_series_equal(result, expected)

result = values.str.contains("a", na=False)
expected = Series([True, False, False, True, False])
tm.assert_series_equal(result, expected)

# na for objects
values = Series(["a", "b", "c", "a", np.nan])
result = values.str.contains("a", na=True)
expected = Series([True, False, False, True, True])
tm.assert_series_equal(result, expected)

result = values.str.contains("a", na=False)
expected = Series([True, False, False, True, False])
tm.assert_series_equal(result, expected)
