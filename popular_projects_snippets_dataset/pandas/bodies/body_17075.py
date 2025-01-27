# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GH#47329
df1 = DataFrame(
    [[0, 1, 1]], columns=Index([1, 2, 3], dtype=any_numeric_ea_dtype)
)
df2 = DataFrame([[0, 1]], columns=Index([1, 2], dtype=any_numeric_ea_dtype))
result = concat([df1, df2], ignore_index=True, join="outer", sort=True)
expected = DataFrame(
    [[0, 1, 1.0], [0, 1, np.nan]],
    columns=Index([1, 2, 3], dtype=any_numeric_ea_dtype),
)
tm.assert_frame_equal(result, expected)
