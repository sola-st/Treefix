# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py

assert NA & True is NA
assert True & NA is NA
assert NA & False is False
assert False & NA is False
assert NA & NA is NA

msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    NA & 5
