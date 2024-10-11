# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# numeric ops on a Series
s = Series(Categorical([1, 2, 3, 4]))
msg = f"Series cannot perform the operation {str_rep}|unsupported operand"
with pytest.raises(TypeError, match=msg):
    getattr(s, op)(2)
