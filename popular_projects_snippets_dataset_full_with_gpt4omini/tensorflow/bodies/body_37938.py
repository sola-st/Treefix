# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
funcs = [
    (np.true_divide, math_ops.truediv),
    (np.floor_divide, math_ops.floordiv),
    (np.true_divide, _TRUEDIV),
    (np.floor_divide, _FLOORDIV),
]
self._testBCastByFunc(funcs, xs, ys)
