# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#22631
box = box_with_array
xbox = np.ndarray if box is pd.array else box

rng = TimedeltaIndex(["1 days", NaT, "2 days"])
expected = NumericIndex([12, np.nan, 24], dtype=np.float64)

rng = tm.box_expected(rng, box)
expected = tm.box_expected(expected, xbox)

other = np.array([2, 4, 2], dtype="m8[h]")
result = rng / other
tm.assert_equal(result, expected)

result = rng / tm.box_expected(other, box)
tm.assert_equal(result, expected)

result = rng / other.astype(object)
tm.assert_equal(result, expected.astype(object))

result = rng / list(other)
tm.assert_equal(result, expected)

# reversed op
expected = 1 / expected
result = other / rng
tm.assert_equal(result, expected)

result = tm.box_expected(other, box) / rng
tm.assert_equal(result, expected)

result = other.astype(object) / rng
tm.assert_equal(result, expected)

result = list(other) / rng
tm.assert_equal(result, expected)
