# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# GH#5206
df = DataFrame(
    np.arange(25).reshape(5, 5), columns="A,B,C,D,E".split(","), dtype=float
)
df["F"] = 99
row_selection = df["A"] % 2 == 0
col_selection = ["B", "C"]
df.loc[row_selection, col_selection] = df["F"]
output = DataFrame(99.0, index=[0, 2, 4], columns=["B", "C"])
tm.assert_frame_equal(df.loc[row_selection, col_selection], output)
self.check(
    target=df,
    indexers=(row_selection, col_selection),
    value=df["F"],
    compare_fn=tm.assert_frame_equal,
    expected=output,
)
