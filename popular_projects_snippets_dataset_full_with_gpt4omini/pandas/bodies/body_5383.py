# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# Ensure timestamps that shouldn't round dont!
# GH#21262

dt = Timestamp(test_input)
expected = Timestamp(expected)
func = getattr(dt, rounder)
result = func(freq)
assert result == expected
