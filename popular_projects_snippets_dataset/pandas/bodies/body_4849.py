# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558
# Not split
s = Series(["abc", "cde", np.nan, "fgh", None], dtype=any_string_dtype)
result = getattr(s.str, method)("_", expand=False)
expected = Series(exp)
tm.assert_series_equal(result, expected)
