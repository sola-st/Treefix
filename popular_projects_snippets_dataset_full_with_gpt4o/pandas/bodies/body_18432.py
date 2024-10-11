# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
tz = tz_naive_fixture

rng = date_range("2000-01-01", "2000-02-01", tz=tz)
expected = date_range("1999-12-31 22:00", "2000-01-31 22:00", tz=tz)

rng = tm.box_expected(rng, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = rng - two_hours
tm.assert_equal(result, expected)

rng -= two_hours
tm.assert_equal(rng, expected)
