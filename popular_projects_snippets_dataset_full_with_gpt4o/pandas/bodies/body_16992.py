# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# GH 18187 regression test
s1 = Series([1])
s2 = Series([], dtype=object)

expected = s1
result = concat([s1, s2])
tm.assert_series_equal(result, expected)
