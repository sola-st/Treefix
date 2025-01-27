# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
td = Timedelta(10, unit="d")

# __neg__, __pos__
assert -td == Timedelta(-10, unit="d")
assert -td == Timedelta("-10d")
assert +td == Timedelta(10, unit="d")

# __abs__, __abs__(__neg__)
assert abs(td) == td
assert abs(-td) == td
assert abs(-td) == Timedelta("10d")
