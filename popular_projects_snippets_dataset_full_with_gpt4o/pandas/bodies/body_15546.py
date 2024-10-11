# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_infer_objects.py
# GH#11221
actual = index_or_series(np.array([1, 2, 3], dtype="O")).infer_objects()
expected = index_or_series([1, 2, 3])
tm.assert_equal(actual, expected)

actual = index_or_series(np.array([1, 2, 3, None], dtype="O")).infer_objects()
expected = index_or_series([1.0, 2.0, 3.0, np.nan])
tm.assert_equal(actual, expected)

# only soft conversions, unconvertable pass thru unchanged

obj = index_or_series(np.array([1, 2, 3, None, "a"], dtype="O"))
actual = obj.infer_objects()
expected = index_or_series([1, 2, 3, None, "a"], dtype=object)

assert actual.dtype == "object"
tm.assert_equal(actual, expected)
