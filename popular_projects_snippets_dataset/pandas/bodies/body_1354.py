# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#14580
# test iloc() on Series with Categorical data

ser = Series([1, 2, 3]).astype("category")

# get slice
result = ser.iloc[0:2]
expected = Series([1, 2]).astype(CategoricalDtype([1, 2, 3]))
tm.assert_series_equal(result, expected)

# get list of indexes
result = ser.iloc[[0, 1]]
expected = Series([1, 2]).astype(CategoricalDtype([1, 2, 3]))
tm.assert_series_equal(result, expected)

# get boolean array
result = ser.iloc[[True, False, False]]
expected = Series([1]).astype(CategoricalDtype([1, 2, 3]))
tm.assert_series_equal(result, expected)
