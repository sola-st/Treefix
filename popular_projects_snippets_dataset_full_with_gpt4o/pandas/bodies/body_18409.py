# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22074, GH#15966
tz = tz_naive_fixture

rng = date_range("1/1/2000", periods=10, tz=tz)
dtarr = tm.box_expected(rng, box_with_array)
assert_invalid_comparison(dtarr, other, box_with_array)
