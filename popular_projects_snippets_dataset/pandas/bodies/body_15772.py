# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# GH#21426
# use int64 bounds and +1 to min_val since true minimum is NaT
# (include min_val/NaT at end to maintain same expected_idxr)
dtype_info = np.iinfo("int64")
min_val, max_val = dtype_info.min, dtype_info.max
vals = [min_val + 1, min_val + 2, max_val - 1, max_val, min_val]
assert_check_nselect_boundary(vals, dtype, nselect_method)
