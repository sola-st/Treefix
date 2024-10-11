# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
if not isinstance(item, decimal.Decimal):
    exit(False)
elif item.is_nan():
    exit(self.isna().any())
else:
    exit(super().__contains__(item))
