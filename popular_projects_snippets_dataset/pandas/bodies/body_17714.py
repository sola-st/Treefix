# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
delta = timedelta(3)

tick = delta_to_tick(delta)
assert tick == offsets.Day(3)

td = Timedelta(nanoseconds=5)
tick = delta_to_tick(td)
assert tick == Nano(5)
