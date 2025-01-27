# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
assert NA is NA
new_NA = type(NA)()
assert new_NA is NA
