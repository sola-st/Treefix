# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop.py
# GH#45860
df = Series(100, index=Index([1, 2, 2], dtype=any_numeric_ea_dtype))
idx = Index([df.index[1]])
result = df.drop(idx)
expected = Series(100, index=Index([1], dtype=any_numeric_ea_dtype))
tm.assert_series_equal(result, expected)
