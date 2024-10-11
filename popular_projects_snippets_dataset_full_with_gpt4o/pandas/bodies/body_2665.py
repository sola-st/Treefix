# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_round.py
# GH#11611

df = DataFrame(
    np.random.random([3, 3]),
    columns=["A", "B", "C"],
    index=["first", "second", "third"],
)

dfs = pd.concat((df, df), axis=1)
rounded = dfs.round()
tm.assert_index_equal(rounded.index, dfs.index)

decimals = Series([1, 0, 2], index=["A", "B", "A"])
msg = "Index of decimals must be unique"
with pytest.raises(ValueError, match=msg):
    df.round(decimals)
