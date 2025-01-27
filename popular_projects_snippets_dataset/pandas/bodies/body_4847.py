# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558
# more than one char
s = Series(["a__b__c", "c__d__e", np.nan, "f__g__h", None], dtype=any_string_dtype)
result = getattr(s.str, method)("__", expand=False)
expected = Series(exp)
tm.assert_series_equal(result, expected)
