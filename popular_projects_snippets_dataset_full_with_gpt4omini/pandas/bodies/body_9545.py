# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
a = TimedeltaArray(pd.timedelta_range("1H", periods=2, freq="H"))
a[0] = Timedelta("1H")
assert a.freq is None
