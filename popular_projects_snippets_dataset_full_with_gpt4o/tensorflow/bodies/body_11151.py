# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Greedily selects a subset of bounding boxes in descending order of score.

  Prunes away boxes that have high overlap with previously selected boxes.
  N-by-n overlap values are supplied as square matrix.
  The output of this operation is a set of integers indexing into the input
  collection of bounding boxes representing the selected boxes.  The bounding
  box coordinates corresponding to the selected indices can then be obtained
  using the `tf.gather` operation.  For example:
    ```python
    selected_indices = tf.image.non_max_suppression_overlaps(
        overlaps, scores, max_output_size, iou_threshold)
    selected_boxes = tf.gather(boxes, selected_indices)
    ```

  Args:
    overlaps: A 2-D float `Tensor` of shape `[num_boxes, num_boxes]`
      representing the n-by-n box overlap values.
    scores: A 1-D float `Tensor` of shape `[num_boxes]` representing a single
      score corresponding to each box (each row of boxes).
    max_output_size: A scalar integer `Tensor` representing the maximum number
      of boxes to be selected by non-max suppression.
    overlap_threshold: A 0-D float tensor representing the threshold for
      deciding whether boxes overlap too much with respect to the provided
      overlap values.
    score_threshold: A 0-D float tensor representing the threshold for deciding
      when to remove boxes based on score.
    name: A name for the operation (optional).

  Returns:
    selected_indices: A 1-D integer `Tensor` of shape `[M]` representing the
      selected indices from the overlaps tensor, where `M <= max_output_size`.
  """
with ops.name_scope(name, 'non_max_suppression_overlaps'):
    overlap_threshold = ops.convert_to_tensor(
        overlap_threshold, name='overlap_threshold')
    # pylint: disable=protected-access
    exit(gen_image_ops.non_max_suppression_with_overlaps(
        overlaps, scores, max_output_size, overlap_threshold, score_threshold))
    # pylint: enable=protected-access
