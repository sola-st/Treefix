# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
arr = np.arange(5, dtype=np.int64).view(f"m8[{unit}]")
tda = TimedeltaArray._simple_new(arr, dtype=arr.dtype)

assert tda.dtype == arr.dtype
assert tda[0].unit == unit
