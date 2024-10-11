# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    with self.cached_session():
        x1 = np.array([-1, 0, 1, 2, 3], dtype=dtype.as_numpy_dtype)
        x2 = np.array([2, 2, 2, 2, 2], dtype=dtype.as_numpy_dtype)
        err = gradient_checker_v2.max_error(
            *gradient_checker_v2.compute_gradient(
                lambda x: math_ops.nextafter(x, x2), [x1]))  # pylint: disable=cell-var-from-loop
        self.assertLess(err, 1e-3)
