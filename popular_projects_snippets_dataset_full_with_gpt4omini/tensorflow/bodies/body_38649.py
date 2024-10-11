# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
with self.cached_session(use_gpu=use_gpu):
    x = ops.convert_to_tensor(x, dtype=dtypes.float64)

    grad_naive_theoretical, _ = gradient_checker_v2.compute_gradient(
        lambda y: math_ops.cumsum(math_ops.exp(y), **kwargs), [x])
    grad_fused_theoretical, _ = gradient_checker_v2.compute_gradient(
        lambda y: math_ops.exp(math_ops.cumulative_logsumexp(y, **kwargs)),
        [x])

    self.assertAllClose(grad_fused_theoretical, grad_naive_theoretical)
