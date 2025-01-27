# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# when sp_index are the same
op = all_arithmetic_functions

values = np.array([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
rvalues = np.array([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])

a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind, fill_value=0)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
