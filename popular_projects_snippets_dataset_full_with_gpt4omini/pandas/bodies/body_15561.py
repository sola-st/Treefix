# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# -----------------------------------------------------------
# floats
floats = Series([1.0, 2.0, 3.0])
result = floats.reindex([1, 2, 3])
expected = Series([2.0, 3.0, np.nan], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

result = floats.reindex([1, 2, 3], fill_value=0)
expected = Series([2.0, 3.0, 0], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

# -----------------------------------------------------------
# ints
ints = Series([1, 2, 3])

result = ints.reindex([1, 2, 3])
expected = Series([2.0, 3.0, np.nan], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

# don't upcast
result = ints.reindex([1, 2, 3], fill_value=0)
expected = Series([2, 3, 0], index=[1, 2, 3])
assert issubclass(result.dtype.type, np.integer)
tm.assert_series_equal(result, expected)

# -----------------------------------------------------------
# objects
objects = Series([1, 2, 3], dtype=object)

result = objects.reindex([1, 2, 3])
expected = Series([2, 3, np.nan], index=[1, 2, 3], dtype=object)
tm.assert_series_equal(result, expected)

result = objects.reindex([1, 2, 3], fill_value="foo")
expected = Series([2, 3, "foo"], index=[1, 2, 3], dtype=object)
tm.assert_series_equal(result, expected)

# ------------------------------------------------------------
# bools
bools = Series([True, False, True])

result = bools.reindex([1, 2, 3])
expected = Series([False, True, np.nan], index=[1, 2, 3], dtype=object)
tm.assert_series_equal(result, expected)

result = bools.reindex([1, 2, 3], fill_value=False)
expected = Series([False, True, False], index=[1, 2, 3])
tm.assert_series_equal(result, expected)
