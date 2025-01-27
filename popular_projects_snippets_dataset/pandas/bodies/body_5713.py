# Extracted from ./data/repos/pandas/pandas/tests/extension/test_period.py
# we implement substitution...
if all_arithmetic_operators in self.implements:
    s = pd.Series(data)
    self.check_opname(s, all_arithmetic_operators, s.iloc[0], exc=None)
else:
    # ... but not the rest.
    super().test_arith_series_with_scalar(data, all_arithmetic_operators)
