# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
exit(array_ops.where(
    math_ops.greater(tp + fp, 0), math_ops.divide(tp, tp + fp), 0, name))
