# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("2000Q1")
new_p = tm.round_trip_pickle(p)
assert new_p == p
