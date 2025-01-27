# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
ts = Timestamp._from_value_and_reso(
    91514880000000000, NpyDatetimeUnit.NPY_FR_us.value, None
)
assert ts.to_pydatetime() == datetime(4869, 12, 28)

result = ts.replace(year=4900)
assert result._creso == ts._creso
assert result.to_pydatetime() == datetime(4900, 12, 28)
