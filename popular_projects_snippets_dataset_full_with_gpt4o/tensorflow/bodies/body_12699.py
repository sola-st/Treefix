# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
features = constant_op.constant([[-2, -1, 1, 3]],
                                dtype=dtypes.float32)
beta = constant_op.constant(0.25, dtype=dtypes.float32)

with self.cached_session():
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        nn_impl.swish, [features, beta])
    error = gradient_checker_v2.max_error(theoretical, numerical)
    self.assertLess(error, 1e-4)
