# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#49034 constructing from a pydate object gets lowest supported
#  reso, i.e. seconds
obj = date(2012, 9, 1)
ts = Timestamp(obj)
assert ts.unit == "s"
