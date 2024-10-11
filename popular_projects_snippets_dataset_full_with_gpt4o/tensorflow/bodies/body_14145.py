# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Creates a `StructuredTensor` from a nonempty dictionary of fields.

    Note that if the shape dtype is not specified, the shape dtype will be
    inferred from any fields that have a shape dtype. If fields differ, then
    int64 will be preferred to int32, because coercing from int32 to int64 is
    safer than coercing from int64 to int32.

    If there are no ragged fields, then it will be int64 by default, but this
    will be changed to int32 in the future.

    Args:
      fields: A dictionary mapping from string to `Tensor`, `RaggedTensor`, or
        `StructuredTensor`, providing the values for individual fields in each
        structure.  If `rank > 0`, then every tensor in `fields` must have the
        same shape in the first `rank` dimensions. Cannot be empty.
      rank: The rank of the resulting structured tensor.
      validate: If true, then add runtime validation ops that check that the
        field values all have compatible shapes in the outer `rank` dimensions.
      dtype: If specified, then forces dtype of the shape to be this.

    Returns:
      A `StructuredTensor`.
    Examples:
      >>> tf.experimental.StructuredTensor.from_fields_and_rank(
      ...     {'x': 1, 'y': [1, 2, 3]}, 0)
      <StructuredTensor(
        fields={
          "x": tf.Tensor(1, shape=(), dtype=int32),
          "y": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},
        shape=())>
      >>> StructuredTensor.from_fields_and_rank({'foo': [1, 2], 'bar': [3, 4]},
      ...                              1)
      <StructuredTensor(
        fields={
          "bar": tf.Tensor([3 4], shape=(2,), dtype=int32),
          "foo": tf.Tensor([1 2], shape=(2,), dtype=int32)},
        shape=(2,))>
    """
if not fields:
    raise ValueError('Must provide at least one field')
if not isinstance(rank, int):
    raise ValueError('rank must be an integer')
if rank < 0:
    raise ValueError('rank must be nonnegative')
fields = {
    k: _convert_to_structured_field_value(v) for (k, v) in fields.items()
}
if dtype is None:
    dtype = _find_shape_dtype(fields, None, None)
fields = _fields_with_dtype(fields, dtype)

shape = _shape_from_fields(fields, rank, dtype)
if rank > 1:
    shape = shape._with_num_row_partitions(rank - 1)
new_rp = shape._row_partitions  # pylint: disable=protected-access
fields = {
    k: _replace_row_partitions(v, new_rp) for (k, v) in fields.items()
}
exit(StructuredTensor(fields=fields, ragged_shape=shape))
