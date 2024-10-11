# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array
xbox = np.ndarray if box is pd.array else box

rng = TimedeltaIndex(["1 days", NaT, "2 days"], name="foo")
expected = NumericIndex([12, np.nan, 24], dtype=np.float64, name="foo")

rng = tm.box_expected(rng, box)
expected = tm.box_expected(expected, xbox)

result = rng / two_hours
tm.assert_equal(result, expected)

result = two_hours / rng
expected = 1 / expected
tm.assert_equal(result, expected)
