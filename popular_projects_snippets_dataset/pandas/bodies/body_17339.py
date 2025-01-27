# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
s = pd.Series(pd.timedelta_range("2000", periods=4))
s.attrs = {"a": 1}
result = method(s.dt)
assert result.attrs == {"a": 1}
