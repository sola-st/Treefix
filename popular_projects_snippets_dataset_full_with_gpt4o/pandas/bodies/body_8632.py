# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
array = np.random.randn(1_000_001)
array2 = np.random.randn(100)

# no op
result = expr._can_use_numexpr(operator.add, None, array, array, "evaluate")
assert not result

# min elements
result = expr._can_use_numexpr(operator.add, "+", array2, array2, "evaluate")
assert not result

# ok, we only check on first part of expression
result = expr._can_use_numexpr(operator.add, "+", array, array2, "evaluate")
assert result
