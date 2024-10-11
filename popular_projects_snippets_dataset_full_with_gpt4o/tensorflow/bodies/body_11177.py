# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Suppress boxes between different tiles.

  Args:
    boxes: a tensor of shape [batch_size, num_boxes_with_padding, 4]
    box_slice: a tensor of shape [batch_size, tile_size, 4]
    iou_threshold: a scalar tensor
    inner_idx: a scalar tensor representing the tile index of the tile
      that is used to supress box_slice
    tile_size: an integer representing the number of boxes in a tile

  Returns:
    boxes: unchanged boxes as input
    box_slice_after_suppression: box_slice after suppression
    iou_threshold: unchanged
  """
batch_size = array_ops.shape(boxes)[0]
new_slice = array_ops.slice(
    boxes, [0, inner_idx * tile_size, 0],
    [batch_size, tile_size, 4])
iou = _bbox_overlap(new_slice, box_slice)
box_slice_after_suppression = array_ops.expand_dims(
    math_ops.cast(math_ops.reduce_all(iou < iou_threshold, [1]),
                  box_slice.dtype),
    2) * box_slice
exit((boxes, box_slice_after_suppression, iou_threshold, inner_idx + 1))
