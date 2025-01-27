# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts this `RaggedTensor` into a `tf.Tensor`.

    If `shape` is specified, then the result is padded and/or truncated to
    the specified shape.

    Examples:

    >>> rt = tf.ragged.constant([[9, 8, 7], [], [6, 5], [4]])
    >>> print(rt.to_tensor())
    tf.Tensor(
        [[9 8 7] [0 0 0] [6 5 0] [4 0 0]], shape=(4, 3), dtype=int32)
    >>> print(rt.to_tensor(shape=[5, 2]))
    tf.Tensor(
        [[9 8] [0 0] [6 5] [4 0] [0 0]], shape=(5, 2), dtype=int32)

    Args:
      default_value: Value to set for indices not specified in `self`. Defaults
        to zero.  `default_value` must be broadcastable to
        `self.shape[self.ragged_rank + 1:]`.
      name: A name prefix for the returned tensors (optional).
      shape: The shape of the resulting dense tensor.  In particular,
        `result.shape[i]` is `shape[i]` (if `shape[i]` is not None), or
        `self.bounding_shape(i)` (otherwise).`shape.rank` must be `None` or
        equal to `self.rank`.

    Returns:
      A `Tensor` with shape `ragged.bounding_shape(self)` and the
      values specified by the non-empty values in `self`.  Empty values are
      assigned `default_value`.
    """
with ops.name_scope(name, "RaggedToTensor", [self, default_value, shape]):
    if default_value is not None:
        default_value = ops.convert_to_tensor(
            default_value, name="default_value", dtype=self.dtype)
    type_tensor_pairs = _get_row_partition_type_tensor_pairs(self)
    row_partition_types = [x[0] for x in type_tensor_pairs]
    row_partition_tensors = [x[1] for x in type_tensor_pairs]
    if default_value is None:
        default_value = array_ops.zeros((), self.dtype)

    if (isinstance(shape, (list, tuple)) and
        any(isinstance(v, ops.Tensor) for v in shape) and
        all(isinstance(v, (int, ops.Tensor)) for v in shape)):
        shape = array_ops.stack(shape)

    shape_tensor = _shape_as_tensor(shape, row_partition_tensors[0].dtype)
    tensor = gen_ragged_conversion_ops.ragged_tensor_to_tensor(
        shape=shape_tensor,
        values=self.flat_values,
        default_value=default_value,
        row_partition_types=row_partition_types,
        row_partition_tensors=row_partition_tensors)

    ragged_shape = self.shape

    if ragged_shape.rank is not None and not isinstance(shape, ops.Tensor):
        # Merged self.shape and shape, favoring the second one as it takes
        # into account potential padding added to the output.
        shape = tensor_shape.as_shape(shape)
        if shape.rank is None:
            output_shape = ragged_shape
        else:
            # At this point we can assume that hshape.rank == ragged_shape.rank
            # because otherwise it would have failed earlier.
            output_shape = [
                s1 if s1 is not None else s2
                for (s1, s2) in zip(shape.as_list(), ragged_shape.as_list())
            ]
        tensor.set_shape(output_shape)

    exit(tensor)
