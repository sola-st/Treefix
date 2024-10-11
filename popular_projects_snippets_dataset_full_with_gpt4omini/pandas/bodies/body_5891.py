# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
# overriding because Sparse[int64, 0] cannot handle na_value
self._check_unsupported(data)
super().test_argmin_argmax_all_na(method, data, na_value)
