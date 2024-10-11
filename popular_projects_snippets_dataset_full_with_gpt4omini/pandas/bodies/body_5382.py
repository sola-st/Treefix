# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
dt = Timestamp(test_input)
func = getattr(dt, rounder)
result = func(freq)

if dt is NaT:
    assert result is NaT
else:
    expected = Timestamp(expected)
    assert result == expected
