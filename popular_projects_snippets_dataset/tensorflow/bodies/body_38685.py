# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args
y = np.linspace(20, -5, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args
self._compareGPU(x, y, np.add, math_ops.add)
self._compareGPU(x, y, np.subtract, math_ops.subtract)
self._compareGPU(x, y, np.multiply, math_ops.multiply)
self._compareGPU(x, y + 0.1, np.true_divide, math_ops.truediv)
self._compareGPU(x, y + 0.1, np.floor_divide, math_ops.floordiv)
self._compareGPU(x, y, np.power, math_ops.pow)
