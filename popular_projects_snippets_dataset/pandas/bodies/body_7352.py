# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#23539 check that a copy isn't made when we pass int64 data
#  and copy=False
arr = np.arange(10, dtype=np.int64)
tdi = TimedeltaIndex(arr, copy=False)
assert tdi._data._ndarray.base is arr
