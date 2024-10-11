# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#50369 We cast to the nearest supported reso, i.e. "s"
ts = to_datetime(dt, errors=errors, cache=cache)
assert isinstance(ts, Timestamp)
assert ts.unit == "s"
assert ts.asm8 == dt

ts = Timestamp(dt)
assert ts.unit == "s"
assert ts.asm8 == dt
