# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
base = datetime(2000, 1, 1)

ts = Timestamp.fromordinal(base.toordinal())
assert base == ts
assert base.toordinal() == ts.toordinal()

ts = Timestamp.fromordinal(base.toordinal(), tz="US/Eastern")
assert Timestamp("2000-01-01", tz="US/Eastern") == ts
assert base.toordinal() == ts.toordinal()

# GH#3042
dt = datetime(2011, 4, 16, 0, 0)
ts = Timestamp.fromordinal(dt.toordinal())
assert ts.to_pydatetime() == dt

# with a tzinfo
stamp = Timestamp("2011-4-16", tz="US/Eastern")
dt_tz = stamp.to_pydatetime()
ts = Timestamp.fromordinal(dt_tz.toordinal(), tz="US/Eastern")
assert ts.to_pydatetime() == dt_tz
