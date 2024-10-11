# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
s = pd.Series(pd.date_range("2000", periods=4))
s.attrs = {"a": 1}
result = getattr(s.dt, attr)
assert result.attrs == {"a": 1}
