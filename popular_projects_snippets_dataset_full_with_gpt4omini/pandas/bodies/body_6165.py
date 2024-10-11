# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
arr = data_missing.take([1, 1])
df = pd.DataFrame({"A": arr})

filled_val = df.iloc[0, 0]
result = df.fillna(filled_val)

assert df.A.values is not result.A.values
