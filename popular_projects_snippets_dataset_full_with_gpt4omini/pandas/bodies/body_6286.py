# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reduce.py
op_name = all_numeric_reductions
s = pd.Series(data)

# min/max with empty produce numpy warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)
    self.check_reduce(s, op_name, skipna)
