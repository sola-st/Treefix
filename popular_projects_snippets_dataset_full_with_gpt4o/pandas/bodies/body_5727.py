# Extracted from ./data/repos/pandas/pandas/tests/extension/list/array.py
exit(np.array(
    [not isinstance(x, list) and np.isnan(x) for x in self.data], dtype=bool
))
