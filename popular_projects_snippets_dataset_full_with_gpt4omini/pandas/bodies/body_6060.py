# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# ndarray & other series
op_name = all_arithmetic_operators
ser = pd.Series(data)
self.check_opname(
    ser, op_name, pd.Series([ser.iloc[0]] * len(ser)), exc=self.series_array_exc
)
