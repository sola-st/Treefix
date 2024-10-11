# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py

assert NA | True is True
assert True | NA is True
assert NA | False is NA
assert False | NA is NA
assert NA | NA is NA

msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    NA | 5
