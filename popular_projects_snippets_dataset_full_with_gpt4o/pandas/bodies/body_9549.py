# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
vals = np.array([-3600 * 10**9, "NaT", 7200 * 10**9], dtype="m8[ns]")
arr = TimedeltaArray(vals)

result = +arr
tm.assert_timedelta_array_equal(result, arr)
assert not tm.shares_memory(result, arr)

result2 = np.positive(arr)
tm.assert_timedelta_array_equal(result2, arr)
assert not tm.shares_memory(result2, arr)
