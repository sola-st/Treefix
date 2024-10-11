# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# frame & scalar
op_name = all_arithmetic_operators
df = pd.DataFrame({"A": data})
self.check_opname(df, op_name, data[0], exc=self.frame_scalar_exc)
