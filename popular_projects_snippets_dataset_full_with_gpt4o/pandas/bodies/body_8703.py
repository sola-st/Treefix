# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data2d = arr1d._ndarray[:3, np.newaxis]
arr2d = type(arr1d)._simple_new(data2d, dtype=arr1d.dtype)
result = list(arr2d)
assert len(result) == 3
for x in result:
    assert isinstance(x, type(arr1d))
    assert x.ndim == 1
    assert x.dtype == arr1d.dtype
