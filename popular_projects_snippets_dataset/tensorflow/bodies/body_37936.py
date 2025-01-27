# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
funcs = [
    (np.subtract, math_ops.subtract),
    (np.subtract, _SUB),
    (np.power, math_ops.pow),
]
self._testBCastByFunc(funcs, xs, ys)
