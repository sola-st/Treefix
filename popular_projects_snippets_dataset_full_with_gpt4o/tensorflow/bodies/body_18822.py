# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Compute the mean intersection-over-union via the confusion matrix."""
sum_over_row = math_ops.cast(
    math_ops.reduce_sum(total_cm, 0), dtypes.float32)
sum_over_col = math_ops.cast(
    math_ops.reduce_sum(total_cm, 1), dtypes.float32)
cm_diag = math_ops.cast(array_ops.diag_part(total_cm), dtypes.float32)
denominator = sum_over_row + sum_over_col - cm_diag

# The mean is only computed over classes that appear in the
# label or prediction tensor. If the denominator is 0, we need to
# ignore the class.
num_valid_entries = math_ops.reduce_sum(
    math_ops.cast(
        math_ops.not_equal(denominator, 0), dtype=dtypes.float32))

# If the value of the denominator is 0, set it to 1 to avoid
# zero division.
denominator = array_ops.where(
    math_ops.greater(denominator, 0), denominator,
    array_ops.ones_like(denominator))
iou = math_ops.divide(cm_diag, denominator)

# If the number of valid entries is 0 (no classes) we return 0.
result = array_ops.where(
    math_ops.greater(num_valid_entries, 0),
    math_ops.reduce_sum(iou, name='mean_iou') / num_valid_entries, 0)
exit(result)
