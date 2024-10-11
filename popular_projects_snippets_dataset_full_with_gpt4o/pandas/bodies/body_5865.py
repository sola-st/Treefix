# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
# https://github.com/pandas-dev/pandas/issues/20762
# This should be the same, aside from concat([sparse, float])
df1 = pd.DataFrame({"A": data[:3]})
df2 = pd.DataFrame({"A": [1, 2, 3]})
df3 = pd.DataFrame({"A": ["a", "b", "c"]}).astype("category")
dfs = [df1, df2, df3]

# dataframes
result = pd.concat(dfs)
expected = pd.concat(
    [x.apply(lambda s: np.asarray(s).astype(object)) for x in dfs]
)
self.assert_frame_equal(result, expected)
