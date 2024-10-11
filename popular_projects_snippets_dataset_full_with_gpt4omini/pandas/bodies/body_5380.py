# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
with tm.assert_produces_warning(False):
    Timestamp("2016-10-17 12:00:00.001501031").round("1010ns")
