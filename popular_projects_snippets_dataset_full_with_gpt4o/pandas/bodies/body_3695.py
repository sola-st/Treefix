# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#22298
df = DataFrame(np.random.normal(size=(10, 2)))
msg = "method must be either 'pearson', 'spearman', 'kendall', or a callable, "
with pytest.raises(ValueError, match=msg):
    df.corr(method="____")
