# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
data = np.array([1, 2, 3], dtype="M8[ns]")
arr = DatetimeArray(data, copy=False)
assert arr._ndarray is data

arr = DatetimeArray(data, copy=True)
assert arr._ndarray is not data
