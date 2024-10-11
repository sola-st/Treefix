# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
if all_arithmetic_operators in self.implements:
    ser = pd.Series(data)
    self.check_opname(ser, all_arithmetic_operators, ser.iloc[0], exc=None)
else:
    # ... but not the rest.
    super().test_arith_series_with_scalar(data, all_arithmetic_operators)
