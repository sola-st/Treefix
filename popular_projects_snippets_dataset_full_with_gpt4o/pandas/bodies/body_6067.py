# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
ser = pd.Series(data)
other = pd.Series([data[0]] * len(data))
self._compare_other(ser, data, comparison_op, other)
