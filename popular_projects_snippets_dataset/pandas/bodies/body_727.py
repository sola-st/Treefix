# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
first = Interval(0, 1, closed="left")
second = Interval(Timestamp(0), Timestamp(1), closed="left")
third = Interval(Timedelta(0), Timedelta(1), closed="left")

arr = np.array([first, second])
assert lib.infer_dtype(arr, skipna=False) == "mixed"

arr = np.array([second, third])
assert lib.infer_dtype(arr, skipna=False) == "mixed"

arr = np.array([first, third])
assert lib.infer_dtype(arr, skipna=False) == "mixed"

# float vs int subdtype are compatible
flt_interval = Interval(1.5, 2.5, closed="left")
arr = np.array([first, flt_interval], dtype=object)
assert lib.infer_dtype(arr, skipna=False) == "interval"
