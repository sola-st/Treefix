# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
x = np.linspace(-5, 20, 15).reshape(3, 5).astype(np.float64)
y = np.linspace(20, -5, 30).reshape(2, 3, 5).astype(np.float64)  # pylint: disable=too-many-function-args
self._compareGPU(x, y, np.add, math_ops.add)
self._compareGPU(x, y, np.subtract, math_ops.subtract)
self._compareGPU(x, y, np.multiply, math_ops.multiply)
self._compareGPU(x, y + 0.1, np.true_divide, math_ops.truediv)
