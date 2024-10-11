# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
ts = tm.makeTimeSeries()
bool_series = ts > 0
assert not bool_series.all()
assert bool_series.any()

# Alternative types, with implicit 'object' dtype.
s = Series(["abc", True])
assert s.any()
