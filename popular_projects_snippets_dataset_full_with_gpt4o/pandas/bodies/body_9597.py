# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py
left = pd.array([1, None, 3, 4], dtype=dtype)
right = pd.array([None, 3, 5, 4], dtype=dtype)

with pytest.raises(TypeError, match="unsupported operand type"):
    left | right
with pytest.raises(TypeError, match="unsupported operand type"):
    left & right
with pytest.raises(TypeError, match="unsupported operand type"):
    left ^ right
