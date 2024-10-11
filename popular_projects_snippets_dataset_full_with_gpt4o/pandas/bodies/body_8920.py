# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# GH 14000
# when sp_index are the same
values = np.array([True, False, True, True], dtype=np.bool_)
rvalues = np.array([True, False, True, True], dtype=np.bool_)

a = SparseArray(values, kind=kind, dtype=np.bool_, fill_value=fill_value)
b = SparseArray(rvalues, kind=kind, dtype=np.bool_, fill_value=fill_value)
self._check_logical_ops(a, b, values, rvalues)
