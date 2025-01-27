# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
self._compareSparseCpu(x, np_func, tf_func, tol)
self._compareSparseGpu(x, np_func, tf_func, tol)
