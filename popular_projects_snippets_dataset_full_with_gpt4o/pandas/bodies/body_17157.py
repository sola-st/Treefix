# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 17038
df2 = DataFrame({cols[0]: [1, 2, 3], cols[1]: [1, 2, 3], "v": [4, 5, 6]})

result = df2.pivot_table(values="v", columns=cols)
expected = DataFrame(
    [[4, 5, 6]],
    columns=MultiIndex.from_tuples([(1, 1), (2, 2), (3, 3)], names=cols),
    index=Index(["v"]),
)

tm.assert_frame_equal(result, expected)
