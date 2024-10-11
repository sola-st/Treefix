# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# e.g. datetime.min
stamp = Timestamp("2012-01-01")

assert not stamp == datetime.min
assert not stamp == datetime(1600, 1, 1)
assert not stamp == datetime(2700, 1, 1)
assert stamp != datetime.min
assert stamp != datetime(1600, 1, 1)
assert stamp != datetime(2700, 1, 1)
assert stamp > datetime(1600, 1, 1)
assert stamp >= datetime(1600, 1, 1)
assert stamp < datetime(2700, 1, 1)
assert stamp <= datetime(2700, 1, 1)

other = Timestamp.min.to_pydatetime(warn=False)
assert other - timedelta(microseconds=1) < Timestamp.min
