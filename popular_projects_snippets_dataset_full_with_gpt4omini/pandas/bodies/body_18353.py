# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
idx = TimedeltaIndex(np.arange(5, dtype="int64"))
idx = tm.box_expected(idx, box_with_array)

result = idx * 1
tm.assert_equal(result, idx)

result = 1 * idx
tm.assert_equal(result, idx)
