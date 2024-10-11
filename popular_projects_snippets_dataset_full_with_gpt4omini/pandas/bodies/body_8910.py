# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
op = all_arithmetic_functions
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
a = SparseArray(values, kind=kind, fill_value=fill_value)
self._check_numeric_ops(a, scalar, values, scalar, mix, op)
