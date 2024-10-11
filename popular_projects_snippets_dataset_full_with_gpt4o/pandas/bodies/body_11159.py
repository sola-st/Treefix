# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 11640

# define the lexsorted version
lexsorted_mi = MultiIndex.from_tuples(
    [("a", ""), ("b1", "c1"), ("b2", "c2")], names=["b", "c"]
)
lexsorted_df = DataFrame([[1, 3, 4]], columns=lexsorted_mi)
assert lexsorted_df.columns._is_lexsorted()

# define the non-lexsorted version
not_lexsorted_df = DataFrame(
    columns=["a", "b", "c", "d"], data=[[1, "b1", "c1", 3], [1, "b2", "c2", 4]]
)
not_lexsorted_df = not_lexsorted_df.pivot_table(
    index="a", columns=["b", "c"], values="d"
)
not_lexsorted_df = not_lexsorted_df.reset_index()
assert not not_lexsorted_df.columns._is_lexsorted()

# compare the results
tm.assert_frame_equal(lexsorted_df, not_lexsorted_df)

expected = lexsorted_df.groupby("a").mean()
with tm.assert_produces_warning(PerformanceWarning):
    result = not_lexsorted_df.groupby("a").mean()
tm.assert_frame_equal(expected, result)

# a transforming function should work regardless of sort
# GH 14776
df = DataFrame(
    {"x": ["a", "a", "b", "a"], "y": [1, 1, 2, 2], "z": [1, 2, 3, 4]}
).set_index(["x", "y"])
assert not df.index._is_lexsorted()

for level in [0, 1, [0, 1]]:
    for sort in [False, True]:
        result = df.groupby(level=level, sort=sort, group_keys=False).apply(
            DataFrame.drop_duplicates
        )
        expected = df
        tm.assert_frame_equal(expected, result)

        result = (
            df.sort_index()
            .groupby(level=level, sort=sort, group_keys=False)
            .apply(DataFrame.drop_duplicates)
        )
        expected = df.sort_index()
        tm.assert_frame_equal(expected, result)
