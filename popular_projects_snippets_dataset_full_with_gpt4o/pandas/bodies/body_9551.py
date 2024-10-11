# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
tdi = pd.timedelta_range("2 Days", periods=4, freq="H")
arr = TimedeltaArray(tdi, freq=tdi.freq)

expected = TimedeltaArray(-tdi._data, freq=-tdi.freq)

result = -arr
tm.assert_timedelta_array_equal(result, expected)

result2 = np.negative(arr)
tm.assert_timedelta_array_equal(result2, expected)
