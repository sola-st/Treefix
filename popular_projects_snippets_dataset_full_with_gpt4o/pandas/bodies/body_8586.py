# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# Explicitly passing freq=None is respected
rng = date_range("1/1/2000", "1/2/2000", freq="5min")

result = DatetimeIndex(rng, freq=None)
assert result.freq is None

result = DatetimeIndex(rng._data, freq=None)
assert result.freq is None

dta = DatetimeArray(rng, freq=None)
assert dta.freq is None
