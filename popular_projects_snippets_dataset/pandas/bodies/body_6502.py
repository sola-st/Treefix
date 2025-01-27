# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
xpr = (
    "Cannot cast data to extension dtype 'decimal'. Pass the "
    "extension array directly."
)
with pytest.raises(ValueError, match=xpr):
    pd.Series([0, 1, 2], dtype=DecimalDtype())
