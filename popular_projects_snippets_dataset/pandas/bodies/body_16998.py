# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# GH21015
s1 = Series({"a": 1, "b": 2}, name=s1name)
s2 = Series({"c": 5, "d": 6}, name=s2name)
result = concat([s1, s2])
expected = Series({"a": 1, "b": 2, "c": 5, "d": 6})
tm.assert_series_equal(result, expected)
