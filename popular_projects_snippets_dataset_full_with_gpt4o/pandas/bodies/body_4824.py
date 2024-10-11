# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# regex split is not supported by rsplit
values = Series(["a,b_c", "c_d,e", np.nan, "f,g,h"], dtype=any_string_dtype)
result = values.str.rsplit("[,_]")
exp = Series([["a,b_c"], ["c_d,e"], np.nan, ["f,g,h"]])
tm.assert_series_equal(result, exp)
