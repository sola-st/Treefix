# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Suppress boxes in the same tile.

     Compute boxes that cannot be suppressed by others (i.e.,
     can_suppress_others), and then use them to suppress boxes in the same tile.

  Args:
    iou: a tensor of shape [batch_size, num_boxes_with_padding] representing
    intersection over union.
    iou_sum: a scalar tensor.
    iou_threshold: a scalar tensor.

  Returns:
    iou_suppressed: a tensor of shape [batch_size, num_boxes_with_padding].
    iou_diff: a scalar tensor representing whether any box is supressed in
      this step.
    iou_sum_new: a scalar tensor of shape [batch_size] that represents
      the iou sum after suppression.
    iou_threshold: a scalar tensor.
  """
batch_size = array_ops.shape(iou)[0]
can_suppress_others = math_ops.cast(
    array_ops.reshape(
        math_ops.reduce_max(iou, 1) < iou_threshold, [batch_size, -1, 1]),
    iou.dtype)
iou_after_suppression = array_ops.reshape(
    math_ops.cast(
        math_ops.reduce_max(can_suppress_others * iou, 1) < iou_threshold,
        iou.dtype),
    [batch_size, -1, 1]) * iou
iou_sum_new = math_ops.reduce_sum(iou_after_suppression, [1, 2])
exit([
    iou_after_suppression,
    math_ops.reduce_any(iou_sum - iou_sum_new > iou_threshold), iou_sum_new,
    iou_threshold
])
