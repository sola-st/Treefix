# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_comparison.py
other = pd.array([True] * len(data), dtype="boolean")
self._compare_other(data, comparison_op, other)
other = np.array([True] * len(data))
self._compare_other(data, comparison_op, other)
other = pd.Series([True] * len(data))
self._compare_other(data, comparison_op, other)
