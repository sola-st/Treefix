# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# GH#21426
dtype_info = np.finfo(float_numpy_dtype)
min_val, max_val = dtype_info.min, dtype_info.max
min_2nd, max_2nd = np.nextafter([min_val, max_val], 0, dtype=float_numpy_dtype)
vals = [min_val, min_2nd, max_2nd, max_val]
assert_check_nselect_boundary(vals, float_numpy_dtype, nselect_method)
