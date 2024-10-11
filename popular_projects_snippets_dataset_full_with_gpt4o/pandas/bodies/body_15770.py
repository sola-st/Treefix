# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# GH#21426
dtype_info = np.iinfo(any_int_numpy_dtype)
min_val, max_val = dtype_info.min, dtype_info.max
vals = [min_val, min_val + 1, max_val - 1, max_val]
assert_check_nselect_boundary(vals, any_int_numpy_dtype, nselect_method)
