# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# GH#4606
p = tm.round_trip_pickle(NaT)
assert p is NaT
