# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
self._compare(sp_t, reduction_axes, ndims, False, False)
self._compare(sp_t, reduction_axes, ndims, False, True)
self._compare(sp_t, reduction_axes, ndims, True, False)
self._compare(sp_t, reduction_axes, ndims, True, True)
