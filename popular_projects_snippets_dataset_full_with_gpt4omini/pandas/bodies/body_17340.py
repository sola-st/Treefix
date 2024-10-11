# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
s = pd.Series(["a", "b"], dtype="category")
s.attrs = {"a": 1}
result = method(s.cat)
assert result.attrs == {"a": 1}
