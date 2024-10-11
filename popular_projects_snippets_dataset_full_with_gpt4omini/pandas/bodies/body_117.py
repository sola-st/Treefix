# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 46719
s = Series([3, "string", float], index=["a", "b", "c"])
result = s.apply(type)
expected = Series([int, str, type], index=["a", "b", "c"])
tm.assert_series_equal(result, expected)
