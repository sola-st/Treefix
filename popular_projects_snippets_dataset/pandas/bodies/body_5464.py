# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
alt = Timestamp(dt64)
result = ts.normalize()
assert result._creso == ts._creso
assert result == alt.normalize()
