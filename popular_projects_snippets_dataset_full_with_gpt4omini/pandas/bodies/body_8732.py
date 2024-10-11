# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH 29578
arr = DatetimeArray(DatetimeIndex(["2019-01-01", NaT]))

result = arr.strftime("%Y-%m-%d")
expected = np.array(["2019-01-01", np.nan], dtype=object)
tm.assert_numpy_array_equal(result, expected)
