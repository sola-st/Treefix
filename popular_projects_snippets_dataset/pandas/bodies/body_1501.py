# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 6546
# setting with mixed labels
df = DataFrame({1: [1, 2], 2: [3, 4], "a": ["a", "b"]})

result = df.loc[0, [1, 2]]
expected = Series(
    [1, 3], index=Index([1, 2], dtype=object), dtype=object, name=0
)
tm.assert_series_equal(result, expected)

expected = DataFrame({1: [5, 2], 2: [6, 4], "a": ["a", "b"]})
df.loc[0, [1, 2]] = [5, 6]
tm.assert_frame_equal(df, expected)
