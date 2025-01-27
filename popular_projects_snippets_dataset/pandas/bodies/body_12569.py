# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# infinities get mapped to nulls which get mapped to NaNs during
# deserialisation
df = DataFrame([[1, 2], [4, 5, 6]])
df.loc[0, 2] = inf
result = read_json(df.to_json(), dtype=dtype)
assert np.isnan(result.iloc[0, 2])
