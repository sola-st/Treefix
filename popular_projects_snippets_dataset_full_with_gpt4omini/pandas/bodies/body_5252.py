# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#46811 don't drop nanos from Timestamp
ts = Timestamp("2022-04-20 09:23:24.123456789")
per = Period(ts, freq="ns")

# should losslessly round-trip, not lose the 789
rt = per.to_timestamp()
assert rt == ts

# same thing but from a datetime64 object
dt64 = ts.asm8
per2 = Period(dt64, freq="ns")
rt2 = per2.to_timestamp()
assert rt2.asm8 == dt64
