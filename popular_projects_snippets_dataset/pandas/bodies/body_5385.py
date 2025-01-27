# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
dt = Timestamp("20130101 09:10:11").as_unit(unit)
result = dt.floor("D")
expected = Timestamp("20130101")
assert result == expected
assert result._creso == dt._creso
