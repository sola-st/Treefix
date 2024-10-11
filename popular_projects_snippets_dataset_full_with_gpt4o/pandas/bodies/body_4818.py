# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# more than one char
values = Series(["a__b__c", "c__d__e", np.nan, "f__g__h"], dtype=any_string_dtype)
result = getattr(values.str, method)("__")
exp = Series([["a", "b", "c"], ["c", "d", "e"], np.nan, ["f", "g", "h"]])
tm.assert_series_equal(result, exp)

result = getattr(values.str, method)("__", expand=False)
tm.assert_series_equal(result, exp)
