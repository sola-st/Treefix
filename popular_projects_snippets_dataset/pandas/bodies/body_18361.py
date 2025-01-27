# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#23829
box = box_with_array
xbox = np.ndarray if box is pd.array else box

rng = timedelta_range("1 days", "10 days")
rng = tm.box_expected(rng, box)

other = np.timedelta64("NaT")

expected = np.array([np.nan] * 10)
expected = tm.box_expected(expected, xbox)

result = rng / other
tm.assert_equal(result, expected)

result = other / rng
tm.assert_equal(result, expected)
