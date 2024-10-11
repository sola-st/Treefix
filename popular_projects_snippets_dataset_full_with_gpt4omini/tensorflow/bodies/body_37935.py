# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
funcs = [
    (np.add, math_ops.add),
    (np.add, _ADD),
]
self._testBCastByFunc(funcs, xs, ys)
