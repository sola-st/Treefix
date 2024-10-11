# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# Explicitly passing freq=None is respected
tdi = timedelta_range(1, periods=5)
assert tdi.freq is not None

result = TimedeltaIndex(tdi, freq=None)
assert result.freq is None

result = TimedeltaIndex(tdi._data, freq=None)
assert result.freq is None

tda = TimedeltaArray(tdi, freq=None)
assert tda.freq is None
