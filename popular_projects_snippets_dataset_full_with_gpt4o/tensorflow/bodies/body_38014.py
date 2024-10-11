# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.linspace(-15, 15, np.prod(xs)).astype(dtype).reshape(xs)
y = np.linspace(20, -10, np.prod(ys)).astype(dtype).reshape(ys)
if dtype in (np.complex64, np.complex128):
    x -= 1j * x
    y -= 1j * y
self._compare(x, y, np_func, tf_func)
self._compare(y, x, np_func, tf_func)
