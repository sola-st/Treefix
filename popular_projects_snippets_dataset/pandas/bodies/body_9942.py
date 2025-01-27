# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
A = series.dropna()
B = (A + np.random.randn(len(A)))[:-5]

result = A.expanding().corr(B)

rolling_result = A.rolling(window=len(A), min_periods=1).corr(B)

tm.assert_almost_equal(rolling_result, result)
