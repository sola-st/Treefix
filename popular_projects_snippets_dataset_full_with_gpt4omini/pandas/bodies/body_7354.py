# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#23539
# fast-path for invalidating a frequency if the passed data already
#  has one and it does not match the `freq` input
tdi = timedelta_range("1 second", periods=100, freq="1s")

msg = (
    "Inferred frequency .* from passed values does "
    "not conform to passed frequency"
)
with pytest.raises(ValueError, match=msg):
    TimedeltaIndex(tdi, freq="D")

with pytest.raises(ValueError, match=msg):
    # GH#23789
    TimedeltaArray(tdi, freq="D")

with pytest.raises(ValueError, match=msg):
    TimedeltaIndex(tdi._data, freq="D")

with pytest.raises(ValueError, match=msg):
    TimedeltaArray(tdi._data, freq="D")
