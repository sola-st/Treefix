# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = array_ops.gather(x, i)
exit(math_ops.cumsum(
    a, axis=axis, exclusive=exclusive, reverse=reverse))
