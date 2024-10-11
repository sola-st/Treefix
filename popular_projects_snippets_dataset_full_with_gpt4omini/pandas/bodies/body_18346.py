# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# only test adding/sub offsets as + is now numeric
# GH#10699 for Tick cases
box = box_with_array
rng = timedelta_range("1 days", "10 days")
expected = timedelta_range("1 days 02:00:00", "10 days 02:00:00", freq="D")
rng = tm.box_expected(rng, box)
expected = tm.box_expected(expected, box)

result = rng + two_hours
tm.assert_equal(result, expected)

result = two_hours + rng
tm.assert_equal(result, expected)
