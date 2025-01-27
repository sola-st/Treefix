# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_sort.py
df1 = DataFrame({"a": [1, 2, 3]}, index=["c", "a", "b"])
df2 = DataFrame({"b": [1, 2]}, index=["a", "b"])

# For True/None
expected = DataFrame(
    {"a": [2, 3, 1], "b": [1, 2, None]},
    index=["a", "b", "c"],
    columns=["a", "b"],
)
if sort is False:
    expected = expected.loc[["c", "a", "b"]]

# Warn and sort by default
with tm.assert_produces_warning(None):
    result = pd.concat([df1, df2], axis=1, sort=sort)
tm.assert_frame_equal(result, expected)
