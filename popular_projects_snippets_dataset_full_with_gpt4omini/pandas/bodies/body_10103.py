# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
A = Series(np.random.randn(50), index=range(50))
B = A[2:] + np.random.randn(48)

A[:10] = np.NaN
B.iloc[-10:] = np.NaN

result = getattr(A.ewm(com=20, min_periods=5), name)(B)
assert np.isnan(result.values[:14]).all()
assert not np.isnan(result.values[14:]).any()
