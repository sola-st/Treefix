# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
self._compareCpu(x, np_func, tf_func, grad_rtol=grad_tol,
                 grad_atol=grad_tol)
self._compareGpu(x, np_func, tf_func)
