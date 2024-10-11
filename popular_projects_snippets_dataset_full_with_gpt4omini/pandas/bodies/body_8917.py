# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([2, np.nan, 2, 3, np.nan, 0, 1, 5, 2, np.nan])

a = SparseArray(values, kind=kind)
b = SparseArray(rvalues, kind=kind)
self._check_comparison_ops(a, b, values, rvalues)
self._check_comparison_ops(a, b * 0, values, rvalues * 0)

a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind)
self._check_comparison_ops(a, b, values, rvalues)

a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind, fill_value=0)
self._check_comparison_ops(a, b, values, rvalues)

a = SparseArray(values, kind=kind, fill_value=1)
b = SparseArray(rvalues, kind=kind, fill_value=2)
self._check_comparison_ops(a, b, values, rvalues)
