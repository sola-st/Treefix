# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# ensure the underlying arrays are properly wrapped as EA when
# constructed from 2D ndarray
arr = np.arange(0, 12, dtype="datetime64[ns]").reshape(4, 3)
df = DataFrame(arr)
assert all(isinstance(arr, DatetimeArray) for arr in df._mgr.arrays)
