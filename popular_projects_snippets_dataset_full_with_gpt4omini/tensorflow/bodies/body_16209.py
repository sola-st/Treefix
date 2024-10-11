# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns the tight bounding box shape for this `RaggedTensor`.

    Args:
      axis: An integer scalar or vector indicating which axes to return the
        bounding box for.  If not specified, then the full bounding box is
        returned.
      name: A name prefix for the returned tensor (optional).
      out_type: `dtype` for the returned tensor.  Defaults to
        `self.row_splits.dtype`.

    Returns:
      An integer `Tensor` (`dtype=self.row_splits.dtype`).  If `axis` is not
      specified, then `output` is a vector with
      `output.shape=[self.shape.ndims]`.  If `axis` is a scalar, then the
      `output` is a scalar.  If `axis` is a vector, then `output` is a vector,
      where `output[i]` is the bounding size for dimension `axis[i]`.

    #### Example:

    >>> rt = tf.ragged.constant([[1, 2, 3, 4], [5], [], [6, 7, 8, 9], [10]])
    >>> rt.bounding_shape().numpy()
    array([5, 4])

    """
if out_type is None:
    out_type = self._row_partition.dtype
else:
    out_type = dtypes.as_dtype(out_type)
with ops.name_scope(name, "RaggedBoundingBox", [self, axis]):
    nested_splits = self.nested_row_splits
    rt_flat_values = self.flat_values

    # Optimized special cases for when axis=0 or axis=1:
    if isinstance(axis, int):
        if axis == 0:
            exit(array_ops.shape(nested_splits[0], out_type=out_type)[0] - 1)
        elif axis == 1:
            result = math_ops.maximum(math_ops.reduce_max(self.row_lengths()), 0)
            if out_type != self._row_partition.dtype:
                result = math_ops.cast(result, out_type)
            exit(result)

    splits_shape = array_ops.shape(self.row_splits, out_type=out_type)
    flat_values_shape = array_ops.shape(rt_flat_values, out_type=out_type)

    ragged_dimensions = [splits_shape[0] - 1] + [
        math_ops.maximum(math_ops.reduce_max(splits[1:] - splits[:-1]), 0)
        for splits in nested_splits
    ]
    inner_dimensions = flat_values_shape[1:]

    if out_type != self._row_partition.dtype:
        ragged_dimensions = [
            math_ops.cast(d, out_type) for d in ragged_dimensions
        ]
    bbox = array_ops.concat(
        [array_ops.stack(ragged_dimensions), inner_dimensions], axis=0)
    exit(bbox if axis is None else array_ops.gather(bbox, axis))
