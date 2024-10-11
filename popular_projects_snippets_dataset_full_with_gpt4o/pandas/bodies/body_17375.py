# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# https://github.com/pydata/xarray/issues/3751
import cftime
import xarray

times = xarray.cftime_range("0001", periods=2)
key = cftime.DatetimeGregorian(2000, 1, 1)
result = times.get_indexer([key], method="nearest")
expected = 1
assert result == expected
