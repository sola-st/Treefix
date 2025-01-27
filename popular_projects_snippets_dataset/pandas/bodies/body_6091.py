# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
result = pd.Series(data)[[0, 1, 3]]
assert result.iloc[0] == data[0]
assert result.iloc[1] == data[1]
assert result.iloc[2] == data[3]
