# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sets_impl.py
"""Compute set intersection of elements in last dimension of `a` and `b`.

  All but the last dimension of `a` and `b` must match.

  Example:

  ```python
    import tensorflow as tf
    import collections

    # Represent the following array of sets as a sparse tensor:
    # a = np.array([[{1, 2}, {3}], [{4}, {5, 6}]])
    a = collections.OrderedDict([
        ((0, 0, 0), 1),
        ((0, 0, 1), 2),
        ((0, 1, 0), 3),
        ((1, 0, 0), 4),
        ((1, 1, 0), 5),
        ((1, 1, 1), 6),
    ])
    a = tf.sparse.SparseTensor(list(a.keys()), list(a.values()),
                               dense_shape=[2,2,2])

    # b = np.array([[{1}, {}], [{4}, {5, 6, 7, 8}]])
    b = collections.OrderedDict([
        ((0, 0, 0), 1),
        ((1, 0, 0), 4),
        ((1, 1, 0), 5),
        ((1, 1, 1), 6),
        ((1, 1, 2), 7),
        ((1, 1, 3), 8),
    ])
    b = tf.sparse.SparseTensor(list(b.keys()), list(b.values()),
                               dense_shape=[2, 2, 4])

    # `tf.sets.intersection` is applied to each aligned pair of sets.
    tf.sets.intersection(a, b)

    # The result will be equivalent to either of:
    #
    # np.array([[{1}, {}], [{4}, {5, 6}]])
    #
    # collections.OrderedDict([
    #     ((0, 0, 0), 1),
    #     ((1, 0, 0), 4),
    #     ((1, 1, 0), 5),
    #     ((1, 1, 1), 6),
    # ])
  ```

  Args:
    a: `Tensor` or `SparseTensor` of the same type as `b`. If sparse, indices
      must be sorted in row-major order.
    b: `Tensor` or `SparseTensor` of the same type as `a`. If sparse, indices
      must be sorted in row-major order.
    validate_indices: Whether to validate the order and range of sparse indices
      in `a` and `b`.

  Returns:
    A `SparseTensor` whose shape is the same rank as `a` and `b`, and all but
    the last dimension the same. Elements along the last dimension contain the
    intersections.
  """
a, b, _ = _convert_to_tensors_or_sparse_tensors(a, b)
exit(_set_operation(a, b, "intersection", validate_indices))
