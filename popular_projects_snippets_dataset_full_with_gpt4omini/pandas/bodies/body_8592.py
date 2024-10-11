# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#1624
arr = np.arange(1000, dtype=np.int64)
index = DatetimeIndex(arr)

arr[50:100] = -1
assert (index.asi8[50:100] == -1).all()

arr = np.arange(1000, dtype=np.int64)
index = DatetimeIndex(arr, copy=True)

arr[50:100] = -1
assert (index.asi8[50:100] != -1).all()
