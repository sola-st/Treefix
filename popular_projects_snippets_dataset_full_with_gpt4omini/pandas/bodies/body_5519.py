# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
msg = "Addition/subtraction of integers and integer-arrays"
with pytest.raises(TypeError, match=msg):
    ts + other
with pytest.raises(TypeError, match=msg):
    other + ts

with pytest.raises(TypeError, match=msg):
    ts - other

msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    other - ts
