# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_ops.py
"""Parses a vector of `SequenceExample` protos.

  Args:
    serialized: A vector (1-D Tensor) of type string, containing binary
      serialized `SequenceExample` protos.
    debug_name: A vector (1-D Tensor) of strings (optional), the names of the
      serialized protos.
    context: A `ParseOpParams` containing the parameters for the parse
      op for the context features.
    feature_list: A `ParseOpParams` containing the parameters for the
      parse op for the feature_list features.
    name: A name for this operation (optional).

  Returns:
    A tuple of three `dict`s, each mapping keys to `Tensor`s, `SparseTensor`s,
    and `RaggedTensor`s. The first dict contains the context key/values, the
    second dict contains the feature_list key/values, and the final dict
    contains the lengths of any dense feature_list features.

  Raises:
    TypeError: if feature_list.dense_defaults is not either None or a dict.
  """
if context.num_features + feature_list.num_features == 0:
    raise ValueError("Must provide at least one feature key.")
with ops.name_scope(name, "ParseSequenceExample", [serialized]):
    debug_name = [] if debug_name is None else debug_name

    # Internal
    feature_list_dense_missing_assumed_empty = []
    for k, v in feature_list.dense_defaults.items():
        if v is not None:
            raise ValueError("Value feature_list.dense_defaults[%s] must be None" %
                             k)
        feature_list_dense_missing_assumed_empty.append(k)

    has_ragged = context.ragged_keys or feature_list.ragged_keys
    serialized = ops.convert_to_tensor(serialized, name="serialized")
    if has_ragged and serialized.shape.ndims is None:
        raise ValueError("serialized must have statically-known rank to "
                         "parse ragged features.")
    feature_list_dense_missing_assumed_empty_vector = [
        key in feature_list_dense_missing_assumed_empty
        for key in feature_list.dense_keys
    ]
    outputs = gen_parsing_ops.parse_sequence_example_v2(
        # Inputs
        serialized=serialized,
        debug_name=debug_name,
        context_sparse_keys=context.sparse_keys,
        context_dense_keys=context.dense_keys,
        context_ragged_keys=context.ragged_keys,
        feature_list_sparse_keys=feature_list.sparse_keys,
        feature_list_dense_keys=feature_list.dense_keys,
        feature_list_ragged_keys=feature_list.ragged_keys,
        feature_list_dense_missing_assumed_empty=(
            feature_list_dense_missing_assumed_empty_vector),
        context_dense_defaults=context.dense_defaults_vec,
        # Attrs
        Ncontext_sparse=len(context.sparse_keys),
        Nfeature_list_sparse=len(feature_list.sparse_keys),
        Nfeature_list_dense=len(feature_list.dense_keys),
        context_sparse_types=context.sparse_types,
        context_ragged_value_types=context.ragged_value_types,
        context_ragged_split_types=context.ragged_split_types,
        feature_list_dense_types=feature_list.dense_types,
        feature_list_sparse_types=feature_list.sparse_types,
        feature_list_ragged_value_types=feature_list.ragged_value_types,
        feature_list_ragged_split_types=feature_list.ragged_split_types,
        context_dense_shapes=context.dense_shapes_as_proto,
        feature_list_dense_shapes=feature_list.dense_shapes,
        name=name)
    (context_sparse_indices, context_sparse_values, context_sparse_shapes,
     context_dense_values, context_ragged_values, context_ragged_row_splits,
     feature_list_sparse_indices, feature_list_sparse_values,
     feature_list_sparse_shapes, feature_list_dense_values,
     feature_list_dense_lengths, feature_list_ragged_values,
     feature_list_ragged_outer_splits,
     feature_list_ragged_inner_splits) = outputs
    # pylint: disable=protected-access
    context_ragged_tensors = parsing_config._build_ragged_tensors(
        serialized.shape, context_ragged_values, context_ragged_row_splits)
    feature_list_ragged_tensors = parsing_config._build_ragged_tensors(
        serialized.shape, feature_list_ragged_values,
        feature_list_ragged_outer_splits, feature_list_ragged_inner_splits)

    # pylint: disable=g-complex-comprehension
    context_sparse_tensors = [
        sparse_tensor.SparseTensor(ix, val, shape)
        for (ix, val,
             shape) in zip(context_sparse_indices, context_sparse_values,
                           context_sparse_shapes)
    ]

    feature_list_sparse_tensors = [
        sparse_tensor.SparseTensor(ix, val, shape)
        for (ix, val, shape
            ) in zip(feature_list_sparse_indices, feature_list_sparse_values,
                     feature_list_sparse_shapes)
    ]
    # pylint: enable=g-complex-comprehension

    context_output = dict(
        zip(
            context.sparse_keys + context.dense_keys + context.ragged_keys,
            context_sparse_tensors + context_dense_values +
            context_ragged_tensors))
    feature_list_output = dict(
        zip(
            feature_list.sparse_keys + feature_list.dense_keys +
            feature_list.ragged_keys, feature_list_sparse_tensors +
            feature_list_dense_values + feature_list_ragged_tensors))
    feature_list_lengths = dict(
        zip(feature_list.dense_keys, feature_list_dense_lengths))

    exit((context_output, feature_list_output, feature_list_lengths))
