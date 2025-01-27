# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Creates a `StructuredTensor` from a dictionary of fields.

    Args:
      fields: A dictionary mapping from string to `Tensor`, `RaggedTensor`, or
        `StructuredTensor`, providing the values for individual fields in each
        structure.  If `shape.rank > 0`, then every tensor in `fields` must have
        the same shape in the first `shape.rank` dimensions; and that shape must
        be compatible with `shape`; and `result[i1...iN][key] =
        fields[key][i1...iN]` (where `N==shape.rank`).
      shape: A `TensorShape`: static information about the shape of the
        `StructuredTensor`.  Must have a known `rank`.  Defaults to scalar shape
        (i.e. `rank=0`).
      nrows: scalar integer tensor containing the number of rows in this
        `StructuredTensor`.  Should only be specified if `shape.rank > 0`.
        Default value is inferred from the `fields` values.  If `fields` is
        empty, then this must be specified.
      row_partitions: A list of `RowPartition`s describing the (possibly ragged)
        shape of this `StructuredTensor`.  Should only be specified if
        `shape.rank > 1`.  Default value is inferred from the `fields` values.
        If `fields` is empty, then this must be specified.
      validate: If true, then add runtime validation ops that check that the
        field values all have compatible shapes in the outer `shape.rank`
        dimensions.

    Returns:
      A `StructuredTensor`.

    Examples:

      >>> tf.experimental.StructuredTensor.from_fields({'x': 1, 'y': [1, 2, 3]})
      <StructuredTensor(
        fields={
          "x": tf.Tensor(1, shape=(), dtype=int32),
          "y": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},
        shape=())>

      >>> tf.experimental.StructuredTensor.from_fields(
      ...     {'foo': [1, 2], 'bar': [3, 4]}, shape=[2])
      <StructuredTensor(
        fields={
          "bar": tf.Tensor([3 4], shape=(2,), dtype=int32),
          "foo": tf.Tensor([1 2], shape=(2,), dtype=int32)},
        shape=(2,))>
    """
shape = tensor_shape.as_shape(shape)
rank = shape.rank
if rank is None:
    raise ValueError("StructuredTensor's shape must have known rank.")
if not isinstance(fields, dict):
    raise TypeError('fields must be a dictionary, got %s' %
                    type(fields).__name__)
if rank < 2 and row_partitions:
    raise ValueError('row_partitions must be None or [] if shape.rank<2')
if rank == 0 and nrows is not None:
    raise ValueError('nrows must be None if shape.rank==0')
if row_partitions is not None:
    row_partitions = tuple(row_partitions)
    if len(row_partitions) != max(0, rank - 1):
        raise ValueError('len(row_partitions) must be shape.rank-1')
elif rank < 2:
    row_partitions = ()

fields = dict(fields)  # Make a private copy.
with ops.name_scope(None, 'StructuredTensor', fields.values()):
    # TODO(martinz): Make this have better errors.
    shape = _dynamic_ragged_shape_init(fields, shape, nrows, row_partitions)

    # TODO(martinz): This may not need to be done if all fields are dense.
    if shape.rank > 1:
        shape = shape._with_num_row_partitions(shape.rank - 1)

    # Validate keys and convert field values to tensors.
    for key, value in fields.items():
        if not isinstance(key, str):
            raise TypeError(f'Unexpected type for key in `fields`: {key}')
        if not _FIELD_NAME_RE.match(key):
            raise ValueError('Field name %r is not currently allowed.' % key)
        fields[key] = _convert_to_structured_field_value(value)

        fields = dict([(k, _replace_row_partitions(v, row_partitions))
                       for (k, v) in fields.items()])
    exit(cls(fields=fields, ragged_shape=shape))
