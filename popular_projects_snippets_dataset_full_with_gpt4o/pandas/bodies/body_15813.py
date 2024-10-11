# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH-19182
ser = Series([True, False, np.nan])
assert ser.dtypes == np.object_

result = ser.astype(CategoricalDtype(categories=[True, False]))
expected = Series(Categorical([True, False, np.nan], categories=[True, False]))
tm.assert_series_equal(result, expected)
