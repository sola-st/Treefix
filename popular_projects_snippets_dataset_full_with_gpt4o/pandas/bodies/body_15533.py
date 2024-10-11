# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py
# GH#15390
original = Series([5, 6, 7])
result = original.clip(upper=upper, inplace=inplace)
expected = Series([1, 2, 3])

if inplace:
    result = original
tm.assert_series_equal(result, expected, check_exact=True)
