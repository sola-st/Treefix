# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# GH#27110 bug in ExtensionBlock.iget caused df.iloc[n] to incorrectly
#  return a scalar
df = pd.DataFrame({"A": data})
expected = pd.Series([data[2]], index=["A"], name=2, dtype=data.dtype)

result = df.loc[2]
self.assert_series_equal(result, expected)

expected = pd.Series(
    [data[-1]], index=["A"], name=len(data) - 1, dtype=data.dtype
)
result = df.iloc[-1]
self.assert_series_equal(result, expected)
