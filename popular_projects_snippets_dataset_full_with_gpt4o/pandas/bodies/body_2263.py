# Extracted from ./data/repos/pandas/pandas/tests/frame/test_ufunc.py
# We don't currently implement
df = pd.DataFrame({"A": [1, 2]})
with pytest.raises(NotImplementedError, match="logaddexp"):
    np.logaddexp(df, df["A"])

with pytest.raises(NotImplementedError, match="logaddexp"):
    np.logaddexp(df["A"], df)
