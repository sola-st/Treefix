# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Compute the mean intersection-over-union via the confusion matrix."""
sum_over_row = math_ops.cast(
    math_ops.reduce_sum(self.total_cm, axis=0), dtype=self._dtype)
sum_over_col = math_ops.cast(
    math_ops.reduce_sum(self.total_cm, axis=1), dtype=self._dtype)
true_positives = math_ops.cast(
    array_ops.tensor_diag_part(self.total_cm), dtype=self._dtype)

# sum_over_row + sum_over_col =
#     2 * true_positives + false_positives + false_negatives.
denominator = sum_over_row + sum_over_col - true_positives

# The mean is only computed over classes that appear in the
# label or prediction tensor. If the denominator is 0, we need to
# ignore the class.
num_valid_entries = math_ops.reduce_sum(
    math_ops.cast(math_ops.not_equal(denominator, 0), dtype=self._dtype))

iou = math_ops.div_no_nan(true_positives, denominator)

exit(math_ops.div_no_nan(
    math_ops.reduce_sum(iou, name='mean_iou'), num_valid_entries))
