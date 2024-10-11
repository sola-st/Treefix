# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558
# unicode
s = Series(["a_b_c", "c_d_e", np.nan, "f_g_h"], dtype=any_string_dtype)

result = getattr(s.str, method)("_", expand=False)
expected = Series(exp)
tm.assert_series_equal(result, expected)
