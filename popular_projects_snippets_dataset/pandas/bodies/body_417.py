# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# GH#43038
assert pandas_dtype(any_real_numpy_dtype) == any_real_numpy_dtype
