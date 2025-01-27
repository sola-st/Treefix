# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# series & scalar
op_name = all_arithmetic_operators
ser = pd.Series(data)
self.check_opname(ser, op_name, ser.iloc[0], exc=self.series_scalar_exc)
