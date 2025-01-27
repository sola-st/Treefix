# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#11640

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

expected = lexsorted_df.drop("a", axis=1)
with tm.assert_produces_warning(PerformanceWarning):
    result = not_lexsorted_df.drop("a", axis=1)

tm.assert_frame_equal(result, expected)
