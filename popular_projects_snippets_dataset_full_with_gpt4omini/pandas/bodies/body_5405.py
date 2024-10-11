# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH: 36294
result = Timestamp("1969-01-01 09:00:00").normalize()
expected = Timestamp("1969-01-01 00:00:00")
assert result == expected
