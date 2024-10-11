# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
empty_series = Series()
assert datetime_series.index._is_all_dates

# Pass in Series
derived = Series(datetime_series)
assert derived.index._is_all_dates

assert tm.equalContents(derived.index, datetime_series.index)
# Ensure new index is not created
assert id(datetime_series.index) == id(derived.index)

# Mixed type Series
mixed = Series(["hello", np.NaN], index=[0, 1])
assert mixed.dtype == np.object_
assert np.isnan(mixed[1])

assert not empty_series.index._is_all_dates
assert not Series().index._is_all_dates

# exception raised is of type ValueError GH35744
with pytest.raises(
    ValueError,
    match=r"Data must be 1-dimensional, got ndarray of shape \(3, 3\) instead",
):
    Series(np.random.randn(3, 3), index=np.arange(3))

mixed.name = "Series"
rs = Series(mixed).name
xp = "Series"
assert rs == xp

# raise on MultiIndex GH4187
m = MultiIndex.from_arrays([[1, 2], [3, 4]])
msg = "initializing a Series from a MultiIndex is not supported"
with pytest.raises(NotImplementedError, match=msg):
    Series(m)
