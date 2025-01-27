# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Replaces by -1 any large out-of-range `values`."""
exit(array_ops.where_v2(math_ops.greater_equal(values, num_classes),
                          -1 * array_ops.ones_like(values), values))
