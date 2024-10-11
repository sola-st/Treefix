# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# setting max number of splits, make sure it's from reverse
values = Series(["a_b_c", "c_d_e", np.nan, "f_g_h"], dtype=any_string_dtype)
result = values.str.rsplit("_", n=1)
exp = Series([["a_b", "c"], ["c_d", "e"], np.nan, ["f_g", "h"]])
tm.assert_series_equal(result, exp)
