# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# Once numpy#17017 is fixed and the xfailed cases in test_nat_comparisons
#  pass, this test can be removed
assert not NaT == other
assert NaT != other
assert not NaT < other
assert not NaT > other
assert not NaT <= other
assert not NaT >= other
