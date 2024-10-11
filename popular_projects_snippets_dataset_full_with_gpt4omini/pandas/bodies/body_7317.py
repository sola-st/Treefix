# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
t1 = timedelta_range("1 days", periods=3, freq="1 min 2 s 3 us")

with pytest.raises(ValueError, match=msg):
    t1.round(freq)
with pytest.raises(ValueError, match=msg):
    # Same test for TimedeltaArray
    t1._data.round(freq)
