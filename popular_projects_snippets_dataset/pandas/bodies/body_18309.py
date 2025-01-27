# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# We don't parametrize this over box_with_array because listlike
#  other plays poorly with assert_invalid_comparison reversed checks

rng = timedelta_range("1 days", periods=10)._data
rng = tm.box_expected(rng, box_with_array)
assert_invalid_comparison(rng, other, box_with_array)
