# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
df1 = DataFrame(np.random.random(size=(10, 2)), columns=["a", "b"])
df2 = DataFrame(np.random.random(size=(10, 3)), columns=["a", "b", "c"])

result = df1.corrwith(df2, drop=False).index.sort_values()
expected = df1.columns.union(df2.columns).sort_values()
tm.assert_index_equal(result, expected)
