# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Calculates the overlap (iou - intersection over union) between boxes_a and boxes_b.

  Args:
    boxes_a: a tensor with a shape of [batch_size, N, 4]. N is the number of
      boxes per image. The last dimension is the pixel coordinates in
      [ymin, xmin, ymax, xmax] form.
    boxes_b: a tensor with a shape of [batch_size, M, 4]. M is the number of
      boxes. The last dimension is the pixel coordinates in
      [ymin, xmin, ymax, xmax] form.
  Returns:
    intersection_over_union: a tensor with as a shape of [batch_size, N, M],
    representing the ratio of intersection area over union area (IoU) between
    two boxes
  """
with ops.name_scope('bbox_overlap'):
    a_y_min, a_x_min, a_y_max, a_x_max = array_ops.split(
        value=boxes_a, num_or_size_splits=4, axis=2)
    b_y_min, b_x_min, b_y_max, b_x_max = array_ops.split(
        value=boxes_b, num_or_size_splits=4, axis=2)

    # Calculates the intersection area.
    i_xmin = math_ops.maximum(
        a_x_min, array_ops.transpose(b_x_min, [0, 2, 1]))
    i_xmax = math_ops.minimum(
        a_x_max, array_ops.transpose(b_x_max, [0, 2, 1]))
    i_ymin = math_ops.maximum(
        a_y_min, array_ops.transpose(b_y_min, [0, 2, 1]))
    i_ymax = math_ops.minimum(
        a_y_max, array_ops.transpose(b_y_max, [0, 2, 1]))
    i_area = math_ops.maximum(
        (i_xmax - i_xmin), 0) * math_ops.maximum((i_ymax - i_ymin), 0)

    # Calculates the union area.
    a_area = (a_y_max - a_y_min) * (a_x_max - a_x_min)
    b_area = (b_y_max - b_y_min) * (b_x_max - b_x_min)
    EPSILON = 1e-8
    # Adds a small epsilon to avoid divide-by-zero.
    u_area = a_area + array_ops.transpose(b_area, [0, 2, 1]) - i_area + EPSILON

    # Calculates IoU.
    intersection_over_union = i_area / u_area

    exit(intersection_over_union)
