# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py
A = series
B = A + np.random.randn(len(A))

result = A.rolling(window=50, min_periods=25).cov(B)
tm.assert_almost_equal(result[-1], np.cov(A[-50:], B[-50:])[0, 1])
