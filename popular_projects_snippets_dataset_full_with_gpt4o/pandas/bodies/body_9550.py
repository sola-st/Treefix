# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
vals = np.array([-3600 * 10**9, "NaT", 7200 * 10**9], dtype="m8[ns]")
arr = TimedeltaArray(vals)

evals = np.array([3600 * 10**9, "NaT", -7200 * 10**9], dtype="m8[ns]")
expected = TimedeltaArray(evals)

result = -arr
tm.assert_timedelta_array_equal(result, expected)

result2 = np.negative(arr)
tm.assert_timedelta_array_equal(result2, expected)
