# Extracted from ./data/repos/pandas/pandas/tests/extension/base/accumulate.py
op_name = all_numeric_accumulations
ser = pd.Series(data)
self.check_accumulate(ser, op_name, skipna)
