# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-#18846
#
# See also test_timedelta.TestTimedeltaArithmetic.test_floordiv
td = Timedelta(hours=3, minutes=4)
assert td // val is expected
