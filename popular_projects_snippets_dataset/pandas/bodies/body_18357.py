# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array
xbox = Series if box in [pd.Index, tm.to_array, pd.array] else box

idx = TimedeltaIndex(np.arange(5, dtype="int64"))
expected = TimedeltaIndex(np.arange(5, dtype="int64") ** 2)

idx = tm.box_expected(idx, box)
expected = tm.box_expected(expected, xbox)

result = idx * Series(np.arange(5, dtype="int64"))
tm.assert_equal(result, expected)
