# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
result = pd.Series(data).apply(id)
assert isinstance(result, pd.Series)
