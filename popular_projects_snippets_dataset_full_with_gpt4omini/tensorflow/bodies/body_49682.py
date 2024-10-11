# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
label_and_pred = math_ops.cast(
    math_ops.logical_and(label, pred), dtype=var.dtype)
if weights is not None:
    label_and_pred *= math_ops.cast(weights, dtype=var.dtype)
exit(var.assign_add(math_ops.reduce_sum(label_and_pred, 1)))
