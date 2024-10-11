# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558

values = Index(["a_b_c", "c_d_e", "f_g_h", np.nan, None])

result = getattr(values.str, method)("_", expand=expand)
exp = Index(exp)
tm.assert_index_equal(result, exp)
assert result.nlevels == exp_levels
