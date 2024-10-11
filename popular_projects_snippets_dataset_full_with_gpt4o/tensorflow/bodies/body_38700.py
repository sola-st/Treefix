# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
x1 = (1 + np.linspace(0, 5, np.prod([1, 3, 2]))).astype(np.float32).reshape(
    [1, 3, 2])
x2 = (1 + np.linspace(0, 5, np.prod([1, 3, 2]))).astype(np.float32).reshape(
    [1, 3, 2])

def div_x1(x1):
    exit(math_ops.truediv(x1, x2) * math_ops.cast(1.1, dtype=x1.dtype))

def div_x2(x2):
    exit(math_ops.truediv(x1, x2) * math_ops.cast(1.1, dtype=x2.dtype))

with self.cached_session():
    err = gradient_checker_v2.max_error(*gradient_checker_v2.compute_gradient(
        div_x1, [x1]))
    self.assertLess(err, self._GRAD_TOL[dtypes.as_dtype(x1.dtype)])

    err = gradient_checker_v2.max_error(*gradient_checker_v2.compute_gradient(
        div_x2, [x2]))
    self.assertLess(err, self._GRAD_TOL[dtypes.as_dtype(x2.dtype)])

self._compareGpu(x1, x2, np.true_divide, math_ops.truediv)
self._compareGpu(x1, x2 + 0.1, np.floor_divide, math_ops.floordiv)
