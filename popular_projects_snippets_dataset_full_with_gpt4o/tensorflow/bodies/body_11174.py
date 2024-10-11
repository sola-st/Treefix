# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Greedily selects a subset of bounding boxes in descending order of score.

  This operation performs non_max_suppression on the inputs per batch, across
  all classes.
  Prunes away boxes that have high intersection-over-union (IOU) overlap
  with previously selected boxes.  Bounding boxes are supplied as
  [y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any
  diagonal pair of box corners and the coordinates can be provided as normalized
  (i.e., lying in the interval [0, 1]) or absolute.  Note that this algorithm
  is agnostic to where the origin is in the coordinate system. Also note that
  this algorithm is invariant to orthogonal transformations and translations
  of the coordinate system; thus translating or reflections of the coordinate
  system result in the same boxes being selected by the algorithm.
  The output of this operation is the final boxes, scores and classes tensor
  returned after performing non_max_suppression.

  Args:
    boxes: A 4-D float `Tensor` of shape `[batch_size, num_boxes, q, 4]`. If `q`
      is 1 then same boxes are used for all classes otherwise, if `q` is equal
      to number of classes, class-specific boxes are used.
    scores: A 3-D float `Tensor` of shape `[batch_size, num_boxes, num_classes]`
      representing a single score corresponding to each box (each row of boxes).
    max_output_size_per_class: A scalar integer `Tensor` representing the
      maximum number of boxes to be selected by non-max suppression per class
    max_total_size: A int32 scalar representing maximum number of boxes retained
      over all classes. Note that setting this value to a large number may
      result in OOM error depending on the system workload.
    iou_threshold: A float representing the threshold for deciding whether boxes
      overlap too much with respect to IOU.
    score_threshold: A float representing the threshold for deciding when to
      remove boxes based on score.
    pad_per_class: If false, the output nmsed boxes, scores and classes are
      padded/clipped to `max_total_size`. If true, the output nmsed boxes,
      scores and classes are padded to be of length
      `max_size_per_class`*`num_classes`, unless it exceeds `max_total_size` in
      which case it is clipped to `max_total_size`. Defaults to false.
    clip_boxes: If true, the coordinates of output nmsed boxes will be clipped
      to [0, 1]. If false, output the box coordinates as it is. Defaults to
      true.
    name: A name for the operation (optional).

  Returns:
    'nmsed_boxes': A [batch_size, max_detections, 4] float32 tensor
      containing the non-max suppressed boxes.
    'nmsed_scores': A [batch_size, max_detections] float32 tensor containing
      the scores for the boxes.
    'nmsed_classes': A [batch_size, max_detections] float32 tensor
      containing the class for boxes.
    'valid_detections': A [batch_size] int32 tensor indicating the number of
      valid detections per batch item. Only the top valid_detections[i] entries
      in nms_boxes[i], nms_scores[i] and nms_class[i] are valid. The rest of the
      entries are zero paddings.
  """
with ops.name_scope(name, 'combined_non_max_suppression'):
    iou_threshold = ops.convert_to_tensor(
        iou_threshold, dtype=dtypes.float32, name='iou_threshold')
    score_threshold = ops.convert_to_tensor(
        score_threshold, dtype=dtypes.float32, name='score_threshold')

    # Convert `max_total_size` to tensor *without* setting the `dtype` param.
    # This allows us to catch `int32` overflow case with `max_total_size`
    # whose expected dtype is `int32` by the op registration. Any number within
    # `int32` will get converted to `int32` tensor. Anything larger will get
    # converted to `int64`. Passing in `int64` for `max_total_size` to the op
    # will throw dtype mismatch exception.
    # TODO(b/173251596): Once there is a more general solution to warn against
    # int overflow conversions, revisit this check.
    max_total_size = ops.convert_to_tensor(max_total_size)

    exit(gen_image_ops.combined_non_max_suppression(
        boxes, scores, max_output_size_per_class, max_total_size, iou_threshold,
        score_threshold, pad_per_class, clip_boxes))
