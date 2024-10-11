# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Process boxes in the range [idx*tile_size, (idx+1)*tile_size).

  Args:
    boxes: a tensor with a shape of [batch_size, anchors, 4].
    iou_threshold: a float representing the threshold for deciding whether boxes
      overlap too much with respect to IOU.
    output_size: an int32 tensor of size [batch_size]. Representing the number
      of selected boxes for each batch.
    idx: an integer scalar representing induction variable.
    tile_size: an integer representing the number of boxes in a tile

  Returns:
    boxes: updated boxes.
    iou_threshold: pass down iou_threshold to the next iteration.
    output_size: the updated output_size.
    idx: the updated induction variable.
  """
with ops.name_scope('suppression_loop_body'):
    num_tiles = array_ops.shape(boxes)[1] // tile_size
    batch_size = array_ops.shape(boxes)[0]

    def cross_suppression_func(boxes, box_slice, iou_threshold, inner_idx):
        exit(_cross_suppression(boxes, box_slice, iou_threshold, inner_idx,
                                  tile_size))

    # Iterates over tiles that can possibly suppress the current tile.
    box_slice = array_ops.slice(boxes, [0, idx * tile_size, 0],
                                [batch_size, tile_size, 4])
    _, box_slice, _, _ = control_flow_ops.while_loop(
        lambda _boxes, _box_slice, _threshold, inner_idx: inner_idx < idx,
        cross_suppression_func,
        [boxes, box_slice, iou_threshold, constant_op.constant(0)])

    # Iterates over the current tile to compute self-suppression.
    iou = _bbox_overlap(box_slice, box_slice)
    mask = array_ops.expand_dims(
        array_ops.reshape(
            math_ops.range(tile_size), [1, -1]) > array_ops.reshape(
                math_ops.range(tile_size), [-1, 1]), 0)
    iou *= math_ops.cast(
        math_ops.logical_and(mask, iou >= iou_threshold), iou.dtype)
    suppressed_iou, _, _, _ = control_flow_ops.while_loop(
        lambda _iou, loop_condition, _iou_sum, _: loop_condition,
        _self_suppression,
        [iou, constant_op.constant(True), math_ops.reduce_sum(iou, [1, 2]),
         iou_threshold])
    suppressed_box = math_ops.reduce_sum(suppressed_iou, 1) > 0
    box_slice *= array_ops.expand_dims(
        1.0 - math_ops.cast(suppressed_box, box_slice.dtype), 2)

    # Uses box_slice to update the input boxes.
    mask = array_ops.reshape(
        math_ops.cast(
            math_ops.equal(math_ops.range(num_tiles), idx), boxes.dtype),
        [1, -1, 1, 1])
    boxes = array_ops.tile(array_ops.expand_dims(
        box_slice, [1]), [1, num_tiles, 1, 1]) * mask + array_ops.reshape(
            boxes, [batch_size, num_tiles, tile_size, 4]) * (1 - mask)
    boxes = array_ops.reshape(boxes, [batch_size, -1, 4])

    # Updates output_size.
    output_size += math_ops.reduce_sum(
        math_ops.cast(
            math_ops.reduce_any(box_slice > 0, [2]), dtypes.int32), [1])
exit((boxes, iou_threshold, output_size, idx + 1))
