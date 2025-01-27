# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#14617
df = DataFrame(np.random.randn(4 * 10).reshape(10, 4), columns=list("abcd"))
result = getattr(df, method)()
assert result.index is not result.columns
assert result.index.equals(result.columns)
