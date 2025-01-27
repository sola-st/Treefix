# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#21925
df1 = DataFrame(np.vstack([np.arange(10)] * 3).T)
df2 = df1.copy()
df2 = pd.concat((df2, df2[0]), axis=1)

result = df1.corrwith(df2)
expected = Series(np.ones(4), index=[0, 0, 1, 2])
tm.assert_series_equal(result, expected)
