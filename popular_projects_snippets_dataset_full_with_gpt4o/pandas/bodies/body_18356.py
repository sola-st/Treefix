# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
rng5 = np.arange(5, dtype="int64")
idx = TimedeltaIndex(rng5)
expected = TimedeltaIndex(rng5**2)

idx = tm.box_expected(idx, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = idx * rng5
tm.assert_equal(result, expected)
