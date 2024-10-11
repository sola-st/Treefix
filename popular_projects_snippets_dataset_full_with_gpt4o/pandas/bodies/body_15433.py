# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
exp = Series(period_range("2000-01-01", periods=10, freq="D"))
exp._values.view("i8")[key] = NaT.value
assert exp[key] is NaT or all(x is NaT for x in exp[key])
exit(exp)
