# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22005, GH#22163 check DataFrame doesn't raise TypeError
tz = tz_naive_fixture

rng = date_range("2000-01-01", "2000-02-01", tz=tz)
expected = date_range("2000-01-01 02:00", "2000-02-01 02:00", tz=tz)

rng = tm.box_expected(rng, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = rng + two_hours
tm.assert_equal(result, expected)

result = two_hours + rng
tm.assert_equal(result, expected)

rng += two_hours
tm.assert_equal(rng, expected)
