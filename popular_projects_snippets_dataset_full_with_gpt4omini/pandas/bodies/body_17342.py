# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
obj.attrs = {"a": 1}
result = method(obj.groupby([0, 0]))
assert result.attrs == {"a": 1}
