# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
ts = Timestamp("2016-01-01")

msg = "Division by zero in rounding"
with pytest.raises(ValueError, match=msg):
    ts.round("0ns")
