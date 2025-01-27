# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
data = np.array([1, 2, 3], dtype="m8[ns]")
arr = TimedeltaArray(data, copy=False)
assert arr._ndarray is data

arr = TimedeltaArray(data, copy=True)
assert arr._ndarray is not data
assert arr._ndarray.base is not data
