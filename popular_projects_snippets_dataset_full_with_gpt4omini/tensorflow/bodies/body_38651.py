# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
exit(map_fn.map_fn(
    lambda i: math_ops.reduce_logsumexp(x[:i + 1]),
    math_ops.range(array_ops.shape(x)[0]),
    dtype=x.dtype))
