# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
# GH 30337
interval = Interval(left, right, closed)
result_dtype, result_value = infer_dtype_from_scalar(interval, pandas_dtype)
expected_dtype = f"interval[{subtype}, {closed}]" if pandas_dtype else np.object_
assert result_dtype == expected_dtype
assert result_value == interval
