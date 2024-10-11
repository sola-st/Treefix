# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# when sp_index are the same
op = all_arithmetic_functions
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])

a = SparseArray(values, kind=kind)
b = SparseArray(rvalues, kind=kind)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
