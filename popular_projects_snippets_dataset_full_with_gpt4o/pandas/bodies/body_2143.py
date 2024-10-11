# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 13180
# coercions from floats/ints are ok
expected = DatetimeIndex(["2015-06-19 05:33:20", "2015-05-27 22:33:20"])
arr = np.array([1.434692e18, 1.432766e18]).astype(dtype)
result = to_datetime(arr, errors=errors, cache=cache)
tm.assert_index_equal(result, expected)
