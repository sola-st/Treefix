# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_sort.py
# GH-4588
df = DataFrame({"c": [1, 2], "b": [3, 4], "a": [5, 6]}, columns=["c", "b", "a"])
result = pd.concat([df, df], sort=True, ignore_index=True)
expected = DataFrame(
    {"a": [5, 6, 5, 6], "b": [3, 4, 3, 4], "c": [1, 2, 1, 2]},
    columns=["a", "b", "c"],
)
tm.assert_frame_equal(result, expected)

result = pd.concat(
    [df, df[["c", "b"]]], join="inner", sort=True, ignore_index=True
)
expected = expected[["b", "c"]]
tm.assert_frame_equal(result, expected)
