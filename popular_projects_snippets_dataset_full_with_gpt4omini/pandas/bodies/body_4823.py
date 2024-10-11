# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
s = Series(["a b", pd.NA, "b c"], dtype=any_string_dtype)
expected = Series([["a", "b"], pd.NA, ["b", "c"]])

result = getattr(s.str, method)(" ", n=n)
tm.assert_series_equal(result, expected)
