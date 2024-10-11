# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
assert hash(NA) == hash(NA)
d = {NA: "test"}
assert d[NA] == "test"
