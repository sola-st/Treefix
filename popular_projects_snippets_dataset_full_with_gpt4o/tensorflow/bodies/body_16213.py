# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Merges outer_axis...inner_axis into a single dimension.

    Returns a copy of this RaggedTensor with the specified range of dimensions
    flattened into a single dimension, with elements in row-major order.

    #### Examples:

    >>> rt = tf.ragged.constant([[[1, 2], [3]], [[4, 5, 6]]])
    >>> print(rt.merge_dims(0, 1))
    <tf.RaggedTensor [[1, 2], [3], [4, 5, 6]]>
    >>> print(rt.merge_dims(1, 2))
    <tf.RaggedTensor [[1, 2, 3], [4, 5, 6]]>
    >>> print(rt.merge_dims(0, 2))
    tf.Tensor([1 2 3 4 5 6], shape=(6,), dtype=int32)

    To mimic the behavior of `np.flatten` (which flattens all dimensions), use
    `rt.merge_dims(0, -1).  To mimic the behavior of `tf.layers.Flatten` (which
    flattens all dimensions except the outermost batch dimension), use
    `rt.merge_dims(1, -1)`.

    Args:
      outer_axis: `int`: The first dimension in the range of dimensions to
        merge. May be negative if `self.shape.rank` is statically known.
      inner_axis: `int`: The last dimension in the range of dimensions to merge.
        May be negative if `self.shape.rank` is statically known.

    Returns:
      A copy of this tensor, with the specified dimensions merged into a
      single dimension.  The shape of the returned tensor will be
      `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N`
      is the total number of slices in the merged dimensions.
    """
outer_axis = array_ops.get_positive_axis(
    outer_axis,
    self.shape.rank,
    axis_name="outer_axis",
    ndims_name="rank(self)")
inner_axis = array_ops.get_positive_axis(
    inner_axis,
    self.shape.rank,
    axis_name="inner_axis",
    ndims_name="rank(self)")
if not outer_axis <= inner_axis:
    raise ValueError(f"Expected outer_axis ({outer_axis}) to be less than or "
                     f"equal to inner_axis ({inner_axis}).")
exit(merge_dims(self, outer_axis, inner_axis))
