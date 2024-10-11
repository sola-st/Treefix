# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array
xbox = Series if box in [pd.Index, tm.to_array, pd.array] else box

idx = TimedeltaIndex(np.arange(5, dtype="int64"))
idx = tm.box_expected(idx, box)

rng5f = np.arange(5, dtype="float64")
expected = TimedeltaIndex(rng5f * (rng5f + 1.0))
expected = tm.box_expected(expected, xbox)

result = idx * Series(rng5f + 1.0)
tm.assert_equal(result, expected)
