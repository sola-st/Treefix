# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
values = Series(["a_b_c", "c_d_e", np.nan, "f_g_h"], dtype=any_string_dtype)

result = getattr(values.str, method)("_")
exp = Series([["a", "b", "c"], ["c", "d", "e"], np.nan, ["f", "g", "h"]])
tm.assert_series_equal(result, exp)
