# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# Overriding this base test to explicitly test that
# the custom _formatter is used
ser = pd.Series(data)
assert data.dtype.name in repr(ser)
assert "Decimal: " in repr(ser)
