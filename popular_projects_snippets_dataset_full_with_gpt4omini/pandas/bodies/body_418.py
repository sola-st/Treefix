# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# GH#43038
assert not pandas_dtype(any_signed_int_ea_dtype) == any_signed_int_numpy_dtype
