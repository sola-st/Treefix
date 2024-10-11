# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

nans = Series(np.NaN, index=datetime_series.index, dtype=np.float64)
assert nans.dtype == np.float_
assert len(nans) == len(datetime_series)

strings = Series("foo", index=datetime_series.index)
assert strings.dtype == np.object_
assert len(strings) == len(datetime_series)

d = datetime.now()
dates = Series(d, index=datetime_series.index)
assert dates.dtype == "M8[ns]"
assert len(dates) == len(datetime_series)

# GH12336
# Test construction of categorical series from value
categorical = Series(0, index=datetime_series.index, dtype="category")
expected = Series(0, index=datetime_series.index).astype("category")
assert categorical.dtype == "category"
assert len(categorical) == len(datetime_series)
tm.assert_series_equal(categorical, expected)
