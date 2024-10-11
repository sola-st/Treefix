# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 28189
# With n_categories as 5, we test the int8 case is hit in libjoin,
# with n_categories as 128 we test the int16 case.
left_index = CategoricalIndex([0] + list(range(n_categories)))
df1 = DataFrame(range(n_categories + 1), columns=["value"], index=left_index)
df2 = DataFrame(
    [[6]],
    columns=["value"],
    index=CategoricalIndex([0], categories=list(range(n_categories))),
)

result = merge(df1, df2, how="left", left_index=True, right_index=True)
expected = DataFrame(
    [[i, 6.0] if i < 2 else [i, np.nan] for i in range(n_categories + 1)],
    columns=["value_x", "value_y"],
    index=left_index,
)
tm.assert_frame_equal(expected, result)
