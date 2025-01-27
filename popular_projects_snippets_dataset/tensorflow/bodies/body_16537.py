# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    x = constant_op.constant([3], dtype=dtype)
    grad = gradient_checker_v2.compute_gradient(
        lambda x: math_ops.reduce_euclidean_norm(x) * 5, [x])
    err = gradient_checker_v2.max_error(*grad)
    self.assertLess(err, 1e-3)
