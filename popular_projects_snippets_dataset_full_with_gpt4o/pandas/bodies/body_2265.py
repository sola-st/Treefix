# Extracted from ./data/repos/pandas/pandas/tests/frame/test_ufunc.py
df = pd.DataFrame({"A": [1, 2]})
with pytest.raises(NotImplementedError, match=""):
    # deprecation enforced in 2.0
    np.subtract.outer(df, df)
