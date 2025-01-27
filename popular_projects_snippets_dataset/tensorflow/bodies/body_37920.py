# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
bf16_np = dtypes_lib.bfloat16.as_numpy_dtype
x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(bf16_np)  # pylint: disable=too-many-function-args
y = np.linspace(20, -5, 15).reshape(1, 3, 5).astype(bf16_np)  # pylint: disable=too-many-function-args
self._compareBoth(x, y, np.add, math_ops.add)
self._compareBoth(x, y, np.subtract, math_ops.subtract)
self._compareBoth(x, y, np.multiply, math_ops.multiply)
self._compareBoth(x, bf16_np(y + 0.1), np.true_divide, math_ops.truediv)
self._compareBoth(x, bf16_np(y + 0.1), np.floor_divide, math_ops.floordiv)
self._compareBoth(x, y, np.add, _ADD)
self._compareBoth(x, y, np.subtract, _SUB)
self._compareBoth(x, y, np.multiply, _MUL)
self._compareBoth(x, bf16_np(y + 0.1), np.true_divide, _TRUEDIV)
self._compareBoth(x, bf16_np(y + 0.1), np.floor_divide, _FLOORDIV)
self._compareBoth(x, y, np.maximum, math_ops.maximum)
self._compareBoth(x, y, np.minimum, math_ops.minimum)
