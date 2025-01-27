# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
result = tm.round_trip_pickle(NA)
assert result is NA
