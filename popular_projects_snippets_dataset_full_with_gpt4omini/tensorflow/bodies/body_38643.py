# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
result_naive = math_ops.cumsum(math_ops.exp(x), **kwargs)
result_fused = math_ops.exp(math_ops.cumulative_logsumexp(x, **kwargs))
exit((result_naive, result_fused))
