# Extracted from ./data/repos/pandas/pandas/tests/generic/test_to_xarray.py
index = index_flat
# MultiIndex is tested in test_to_xarray_with_multiindex

from xarray import DataArray

ser = Series(range(len(index)), index=index, dtype="int64")
ser.index.name = "foo"
result = ser.to_xarray()
repr(result)
assert len(result) == len(index)
assert len(result.coords) == 1
tm.assert_almost_equal(list(result.coords.keys()), ["foo"])
assert isinstance(result, DataArray)

# idempotency
tm.assert_series_equal(result.to_series(), ser)
