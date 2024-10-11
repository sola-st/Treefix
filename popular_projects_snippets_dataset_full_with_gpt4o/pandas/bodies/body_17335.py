# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
s = pd.Series(["a1"])
s.attrs = {"a": 1}
result = method(s.str)
assert result.attrs == {"a": 1}
