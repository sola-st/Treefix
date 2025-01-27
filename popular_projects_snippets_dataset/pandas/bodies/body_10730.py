# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
df = DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df["A"] = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]

gb = df.groupby("A")

res = gb.idxmax(axis=1)

alt = df.iloc[:, 1:].idxmax(axis=1)
indexer = res.index.get_level_values(1)

tm.assert_series_equal(alt[indexer], res.droplevel("A"))

df["E"] = date_range("2016-01-01", periods=10)
gb2 = df.groupby("A")

msg = "reduction operation 'argmax' not allowed for this dtype"
with pytest.raises(TypeError, match=msg):
    gb2.idxmax(axis=1)
