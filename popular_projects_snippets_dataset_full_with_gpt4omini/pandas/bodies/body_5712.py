# Extracted from ./data/repos/pandas/pandas/tests/extension/test_period.py
# frame & scalar
if all_arithmetic_operators in self.implements:
    df = pd.DataFrame({"A": data})
    self.check_opname(df, all_arithmetic_operators, data[0], exc=None)
else:
    # ... but not the rest.
    super().test_arith_frame_with_scalar(data, all_arithmetic_operators)
