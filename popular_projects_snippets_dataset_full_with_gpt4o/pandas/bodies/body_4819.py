# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# regex split
values = Series(["a,b_c", "c_d,e", np.nan, "f,g,h"], dtype=any_string_dtype)
result = values.str.split("[,_]")
exp = Series([["a", "b", "c"], ["c", "d", "e"], np.nan, ["f", "g", "h"]])
tm.assert_series_equal(result, exp)
