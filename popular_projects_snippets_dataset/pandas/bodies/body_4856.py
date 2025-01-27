# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# GH 12617
# should preserve name
s = Series(["a,b", "c,d"], name="xxx", dtype=any_string_dtype)
result = s.str.partition(",", expand=False)
expected = Series([("a", ",", "b"), ("c", ",", "d")], name="xxx")
tm.assert_series_equal(result, expected)
