# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH#14621, GH#7825
ts = Timestamp("2016-01-01 09:00:00")
result = ts.replace(hour=0)
expected = Timestamp("2016-01-01 00:00:00")
assert result == expected
