# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
exit(array_ops.where(
    math_ops.greater(true_p + false_n, 0),
    math_ops.divide(true_p, true_p + false_n), 0, name))
