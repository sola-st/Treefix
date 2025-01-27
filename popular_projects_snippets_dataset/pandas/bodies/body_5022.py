# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
# GH 30013
result = {NA, hash(NA)}

assert len(result) == 2
assert NA in result
assert hash(NA) in result
