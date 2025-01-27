# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reduce.py
op_name = all_boolean_reductions
s = pd.Series(data)
self.check_reduce(s, op_name, skipna)
