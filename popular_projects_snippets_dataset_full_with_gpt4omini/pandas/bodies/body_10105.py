# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
A = Series(np.random.randn(50), index=range(50))
A[:10] = np.NaN

msg = "other must be a DataFrame or Series"
# exception raised is Exception
with pytest.raises(ValueError, match=msg):
    getattr(A.ewm(com=20, min_periods=5), name)(np.random.randn(50))
