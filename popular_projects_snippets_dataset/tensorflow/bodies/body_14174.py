# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Merges outer_axis...inner_axis into a single dimension.

    Returns a copy of this RaggedTensor with the specified range of dimensions
    flattened into a single dimension, with elements in row-major order.

    >>> st = tf.experimental.StructuredTensor.from_pyval(
    ...     [[{'foo': 12}, {'foo': 33}], [], [{'foo': 99}]])
    >>> st.merge_dims(0, 1)
    <StructuredTensor(
      fields={
        "foo": tf.Tensor([12 33 99], shape=(3,), dtype=int32)},
      shape=(3,))>

    Args:
      outer_axis: `int`: The first dimension in the range of dimensions to
        merge. May be negative (to index from the last dimension).
      inner_axis: `int`: The last dimension in the range of dimensions to merge.
        May be negative (to index from the last dimension).

    Returns:
      A copy of this tensor, with the specified dimensions merged into a
      single dimension.  The shape of the returned tensor will be
      `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N`
      is the total number of slices in the merged dimensions.
    """
outer_axis = array_ops.get_positive_axis(
    outer_axis,
    self.shape.rank,
    axis_name='outer_axis',
    ndims_name='rank(self)')
inner_axis = array_ops.get_positive_axis(
    inner_axis,
    self.shape.rank,
    axis_name='inner_axis',
    ndims_name='rank(self)')
if not outer_axis <= inner_axis:
    raise ValueError('Expected outer_axis (%d) to be less than or equal to '
                     'inner_axis (%d)' % (outer_axis, inner_axis))
exit(_merge_dims(self, outer_axis, inner_axis))
