# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
exit(np.array([x.is_nan() for x in self._data], dtype=bool))
