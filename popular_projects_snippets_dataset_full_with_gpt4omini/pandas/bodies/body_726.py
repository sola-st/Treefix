# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

first = Interval(value, value, closed="left")
second = Interval(value, value, closed="right")

# if closed match, we should infer "interval"
arr = np.array([first, first], dtype=object)
assert lib.infer_dtype(arr, skipna=False) == "interval"

# if closed dont match, we should _not_ get "interval"
arr2 = np.array([first, second], dtype=object)
assert lib.infer_dtype(arr2, skipna=False) == "mixed"
