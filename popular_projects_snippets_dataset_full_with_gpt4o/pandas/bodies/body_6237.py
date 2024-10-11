# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
s = pd.Series(data)
result = s.memory_usage(index=False)
assert result == s.nbytes
