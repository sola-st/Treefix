# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
funcs = [
    (np.multiply, math_ops.multiply),
    (np.multiply, _MUL),
]
self._testBCastByFunc(funcs, xs, ys)
