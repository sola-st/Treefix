# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
jan = Period("2000-01", "M")
feb = Period("2000-02", "M")

assert not jan == feb
assert jan != feb
assert jan < feb
assert jan <= feb
assert not jan > feb
assert not jan >= feb
