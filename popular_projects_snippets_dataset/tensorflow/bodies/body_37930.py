# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = (1 + 1j) * np.linspace(-10, 10, 6).reshape(1, 3, 2).astype(  # pylint: disable=too-many-function-args
    np.complex128)
y = (1 + 1j) * np.linspace(20, -20, 6).reshape(1, 3, 2).astype(  # pylint: disable=too-many-function-args
    np.complex128)
self._compareBoth(x, y, np.add, math_ops.add)
self._compareBoth(x, y, np.subtract, math_ops.subtract)
self._compareBoth(x, y, np.multiply, math_ops.multiply)
self._compareBoth(x, y + 0.1, np.true_divide, math_ops.truediv)
self._compareBoth(x, y, np.add, _ADD)
self._compareBoth(x, y, np.subtract, _SUB)
self._compareBoth(x, y, np.multiply, _MUL)
self._compareBoth(x, y + 0.1, np.true_divide, _TRUEDIV)
