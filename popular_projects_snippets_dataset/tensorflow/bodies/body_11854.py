# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
exit(math_ops.logical_and(
    math_ops.less(i, max_it),
    math_ops.less(abs_tol, math_ops.reduce_max(upper - lower))))
