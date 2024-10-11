# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
# https://github.com/pandas-dev/pandas/issues/18888
exp = frame_or_series(
    pd.Categorical(["A", "A", "B", "B", np.nan], categories=["A", "B", "C"]),
    dtype="category",
)
df = frame_or_series(["A", "A", "B", "B", "C"], dtype="category")
res = df.where(df != "C")
tm.assert_equal(exp, res)
