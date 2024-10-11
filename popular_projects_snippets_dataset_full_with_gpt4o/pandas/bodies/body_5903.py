# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
arr = data_for_compare + 1
self._compare_other(data_for_compare, comparison_op, arr)
arr = data_for_compare * 2
self._compare_other(data_for_compare, comparison_op, arr)
