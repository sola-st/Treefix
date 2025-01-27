# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH 12814, unorderable types in py3 with a non-unique index
df1 = DataFrame({"a": [1, 2, 3, 4]}, index=[1, 2, 3, "a"])
df2 = DataFrame({"b": [5, 6, 7, 8]}, index=[1, 3, 3, 4])
result = df1.join(df2)
expected = DataFrame(
    {"a": [1, 2, 3, 3, 4], "b": [5, np.nan, 6, 7, np.nan]},
    index=[1, 2, 3, 3, "a"],
)
tm.assert_frame_equal(result, expected)

df3 = DataFrame({"a": [1, 2, 3, 4]}, index=[1, 2, 2, "a"])
df4 = DataFrame({"b": [5, 6, 7, 8]}, index=[1, 2, 3, 4])
result = df3.join(df4)
expected = DataFrame(
    {"a": [1, 2, 3, 4], "b": [5, 6, 6, np.nan]}, index=[1, 2, 2, "a"]
)
tm.assert_frame_equal(result, expected)
