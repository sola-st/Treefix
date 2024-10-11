# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# This is a dtype-specific test that ensures Series[decimal].astype
# gets all the way through to ExtensionArray.astype
# Designing a reliable smoke test that works for arbitrary data types
# is difficult.
data = pd.Series(DecimalArray([decimal.Decimal(2)]), name="a")
ctx = decimal.Context()
ctx.prec = 5

if frame:
    data = data.to_frame()

result = data.astype(DecimalDtype(ctx))

if frame:
    result = result["a"]

assert result.dtype.context.prec == ctx.prec
