# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_sort.py
# GH-4588
df1 = DataFrame({"a": [1, 2], "b": [1, 2]}, columns=["b", "a"])
df2 = DataFrame({"a": [3, 4], "c": [5, 6]})

# for sort=True/None
expected = DataFrame(
    {"a": [1, 2, 3, 4], "b": [1, 2, None, None], "c": [None, None, 5, 6]},
    columns=["a", "b", "c"],
)

if sort is False:
    expected = expected[["b", "a", "c"]]

# default
with tm.assert_produces_warning(None):
    result = pd.concat([df1, df2], ignore_index=True, sort=sort)
tm.assert_frame_equal(result, expected)
