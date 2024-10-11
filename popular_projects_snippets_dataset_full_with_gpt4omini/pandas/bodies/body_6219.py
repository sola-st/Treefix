# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
result = pd.Series(data).tolist()
expected = list(data)
assert result == expected
