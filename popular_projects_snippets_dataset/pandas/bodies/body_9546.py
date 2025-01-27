# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
# make sure we accept timedelta64 and timedelta in addition to Timedelta
tdi = pd.timedelta_range("2 Days", periods=4, freq="H")
arr = TimedeltaArray(tdi, freq=tdi.freq)

arr[0] = obj
assert arr[0] == Timedelta(seconds=1)
