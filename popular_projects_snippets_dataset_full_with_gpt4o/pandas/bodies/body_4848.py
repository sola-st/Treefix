# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558
# None
s = Series(["a b c", "c d e", np.nan, "f g h", None], dtype=any_string_dtype)
result = getattr(s.str, method)(expand=False)
expected = Series(exp)
tm.assert_series_equal(result, expected)
