# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_cov_corr.py
# GH PR #22298
s1 = Series(np.random.randn(10))
s2 = Series(np.random.randn(10))
msg = "method must be either 'pearson', 'spearman', 'kendall', or a callable, "
with pytest.raises(ValueError, match=msg):
    s1.corr(s2, method="____")
