# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
"""
    Fixture giving a numpy array and a parametrized 'data' object, which can
    be a memoryview, array, dask or xarray object created from the numpy array.
    """
# GH#24539 recognize e.g xarray, dask, ...
arr = np.array([1, 2, 3], dtype=np.int64)

name = request.param
if name == "memoryview":
    data = memoryview(arr)
elif name == "array":
    data = array.array("i", arr)
elif name == "dask":
    import dask.array

    data = dask.array.array(arr)
elif name == "xarray":
    import xarray as xr

    data = xr.DataArray(arr)

exit((arr, data))
