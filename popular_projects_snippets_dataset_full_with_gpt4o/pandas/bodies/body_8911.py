# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])

a = SparseArray(values, kind=kind)
self._check_comparison_ops(a, 1, values, 1)
self._check_comparison_ops(a, 0, values, 0)
self._check_comparison_ops(a, 3, values, 3)

a = SparseArray(values, kind=kind, fill_value=0)
self._check_comparison_ops(a, 1, values, 1)
self._check_comparison_ops(a, 0, values, 0)
self._check_comparison_ops(a, 3, values, 3)

a = SparseArray(values, kind=kind, fill_value=2)
self._check_comparison_ops(a, 1, values, 1)
self._check_comparison_ops(a, 0, values, 0)
self._check_comparison_ops(a, 3, values, 3)
