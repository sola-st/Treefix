# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#21925
df = DataFrame(np.random.random(size=(100, 3)))
result = df.corrwith(df**2, method="spearman")
expected = Series(np.ones(len(result)))
tm.assert_series_equal(result, expected)
