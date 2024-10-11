# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
df1 = DataFrame({"a": [1, 2], "b": [1, 2]}, columns=["b", "a"])
df2 = DataFrame({"a": [1, 2], "c": [3, 4]}, index=[2, 3])

result = df1._append(df2, sort=sort)

# for None / True
expected = DataFrame(
    {"b": [1, 2, None, None], "a": [1, 2, 1, 2], "c": [None, None, 3, 4]},
    columns=["a", "b", "c"],
)
if sort is False:
    expected = expected[["b", "a", "c"]]
tm.assert_frame_equal(result, expected)
