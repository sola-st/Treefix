# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
idx = MultiIndex(
    codes=[[0, 0, 0], [0, 1, 1], [1, 0, 1]],
    levels=[["a", "b"], ["x", "y"], ["p", "q"]],
)
df = DataFrame(np.random.rand(3, 2), index=idx)

result = df.loc[("a", "y"), :]
expected = df.loc[("a", "y")]
tm.assert_frame_equal(result, expected)

result = df.loc[("a", "y"), [1, 0]]
expected = df.loc[("a", "y")][[1, 0]]
tm.assert_frame_equal(result, expected)

with pytest.raises(KeyError, match=r"\('a', 'foo'\)"):
    df.loc[("a", "foo"), :]
