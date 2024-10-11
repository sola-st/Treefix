# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# when sp_index are the same
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])

a = SparseArray(values, kind=kind)
b = SparseArray(rvalues, kind=kind)
self._check_comparison_ops(a, b, values, rvalues)

values = np.array([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
rvalues = np.array([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])

a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind, fill_value=0)
self._check_comparison_ops(a, b, values, rvalues)
