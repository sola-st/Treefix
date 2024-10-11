# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# only test adding/sub offsets as - is now numeric
rng = timedelta_range("1 days", "10 days")
expected = timedelta_range("0 days 22:00:00", "9 days 22:00:00")

rng = tm.box_expected(rng, box_with_array)
expected = tm.box_expected(expected, box_with_array)

orig_rng = rng
rng -= two_hours
tm.assert_equal(rng, expected)
if box_with_array is not pd.Index:
    # Check that operation is actually inplace
    tm.assert_equal(orig_rng, expected)
