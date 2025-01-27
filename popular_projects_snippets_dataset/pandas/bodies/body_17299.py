# Extracted from ./data/repos/pandas/pandas/tests/generic/test_to_xarray.py
from xarray import DataArray

ser = Series([], dtype=object)
ser.index.name = "foo"
result = ser.to_xarray()
assert len(result) == 0
assert len(result.coords) == 1
tm.assert_almost_equal(list(result.coords.keys()), ["foo"])
assert isinstance(result, DataArray)
