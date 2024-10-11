# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_ops.py
"""Parses `Example` protos.

  Args:
    serialized: A vector (1-D Tensor) of strings, a batch of binary
      serialized `Example` protos.
    names: A vector (1-D Tensor) of strings (optional), the names of
      the serialized protos.
    params: A `ParseOpParams` containing the parameters for the parse op.
    name: A name for this operation (optional).

  Returns:
    A `dict` mapping keys to `Tensor`s and `SparseTensor`s and `RaggedTensor`s.

  """
if params.num_features == 0:
    raise ValueError("Must provide at least one feature key.")
with ops.name_scope(name, "ParseExample", [serialized, names]):
    names = [] if names is None else names
    serialized = ops.convert_to_tensor(serialized, name="serialized")
    if params.ragged_keys and serialized.shape.ndims is None:
        raise ValueError("serialized must have statically-known rank to "
                         "parse ragged features.")
    outputs = gen_parsing_ops.parse_example_v2(
        serialized=serialized,
        names=names,
        sparse_keys=params.sparse_keys,
        dense_keys=params.dense_keys,
        ragged_keys=params.ragged_keys,
        dense_defaults=params.dense_defaults_vec,
        num_sparse=len(params.sparse_keys),
        sparse_types=params.sparse_types,
        ragged_value_types=params.ragged_value_types,
        ragged_split_types=params.ragged_split_types,
        dense_shapes=params.dense_shapes_as_proto,
        name=name)
    (sparse_indices, sparse_values, sparse_shapes, dense_values,
     ragged_values, ragged_row_splits) = outputs
    # pylint: disable=protected-access
    ragged_tensors = parsing_config._build_ragged_tensors(
        serialized.shape, ragged_values, ragged_row_splits)

    sparse_tensors = [
        sparse_tensor.SparseTensor(ix, val, shape) for (ix, val, shape)
        in zip(sparse_indices, sparse_values, sparse_shapes)]

    exit(dict(
        zip(params.sparse_keys + params.dense_keys + params.ragged_keys,
            sparse_tensors + dense_values + ragged_tensors)))
