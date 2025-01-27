# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
dt = Timestamp(timestamp)
result = dt.round(freq)
expected = Timestamp(expected)
assert result == expected
