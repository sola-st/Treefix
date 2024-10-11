# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#23539
# fast-path for inferring a frequency if the passed data already
#  has one
tdi = timedelta_range("1 second", periods=10**7, freq="1s")

result = TimedeltaIndex(tdi, freq="infer")
assert result.freq == tdi.freq

# check that inferred_freq was not called by checking that the
#  value has not been cached
assert "inferred_freq" not in getattr(result, "_cache", {})
