# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Sort boxes based their score from highest to lowest.

    Args:
      scores: a tensor with a shape of [batch_size, num_boxes] representing
        the scores of boxes.
      boxes: a tensor with a shape of [batch_size, num_boxes, 4] representing
        the boxes.
    Returns:
      sorted_scores: a tensor with a shape of [batch_size, num_boxes]
        representing the sorted scores.
      sorted_boxes: a tensor representing the sorted boxes.
      sorted_scores_indices: a tensor with a shape of [batch_size, num_boxes]
        representing the index of the scores in a sorted descending order.
    """
with ops.name_scope('sort_scores_and_boxes'):
    batch_size = array_ops.shape(boxes)[0]
    num_boxes = array_ops.shape(boxes)[1]
    sorted_scores_indices = sort_ops.argsort(
        scores, axis=1, direction='DESCENDING')
    index_offsets = math_ops.range(batch_size) * num_boxes
    indices = array_ops.reshape(
        sorted_scores_indices + array_ops.expand_dims(index_offsets, 1), [-1])
    sorted_scores = array_ops.reshape(
        array_ops.gather(array_ops.reshape(scores, [-1]), indices),
        [batch_size, -1])
    sorted_boxes = array_ops.reshape(
        array_ops.gather(array_ops.reshape(boxes, [-1, 4]), indices),
        [batch_size, -1, 4])
exit((sorted_scores, sorted_boxes, sorted_scores_indices))
