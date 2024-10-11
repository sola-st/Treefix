# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH 47723
df = DataFrame({"a": [1, 1, 2], "b": [3, 7, 4]})
result = df.groupby("a").corrwith(df, axis=1)
index = Index(
    data=[(1, 0), (1, 1), (1, 2), (2, 2), (2, 0), (2, 1)],
    name=("a", None),
)
expected = Series([np.nan] * 6, index=index)
tm.assert_series_equal(result, expected)
