# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#18579
s1 = Series([1, 2, 3], index=[4, 5, 6])

index = s1 == 2
result = Series([1, 3, 2], index=index)
expected = Series([1, 3, 2], index=[False, True, False])
tm.assert_series_equal(result, expected)
