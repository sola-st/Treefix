# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Outputs a the enqueue op given the inputs and weights.

    Args:
      flat_inputs: A list of input tensors.
      flat_weights: A list of input weights (or None) of the same length as
        flat_inputs.
      flat_features: A list of FeatureConfigs of the same length as flat_inputs.
      device_ordinal: The device to create the enqueue op for.
      mode_override: A tensor containing the string "train" or "inference".

    Returns:
      The enqueue op.
    """
# Combiners are per table, list in the same order as the table order.
combiners = [table.combiner for table in self._table_config]

# These parallel arrays will be the inputs to the enqueue op.
# sample_indices for sparse, row_splits for ragged.
indices_or_row_splits = []
values = []
weights = []

# We have to supply a empty/zero tensor in a list position where we don't
# have data (e.g. indices for standard Tensor input, weight when no weight
# is specified). We create one op here per call, so that we reduce the
# graph size.
int_zeros = array_ops.zeros((0,), dtype=dtypes.int32)
float_zeros = array_ops.zeros((0,), dtype=dtypes.float32)

# In the following loop we insert casts so that everything is either int32
# or float32. This is because op inputs which are lists of tensors must be
# of the same type within the list. Moreover the CPU implementations of
# these ops cast to these types anyway, so we don't lose any data by casting
# early.
for inp, weight, (path, feature) in zip(
    flat_inputs, flat_weights, flat_features):
    if isinstance(inp, ops.Tensor):
        self._add_data_for_tensor(inp, weight, indices_or_row_splits, values,
                                  weights, int_zeros, float_zeros, path)
    elif isinstance(inp, sparse_tensor.SparseTensor):
        self._add_data_for_sparse_tensor(inp, weight, indices_or_row_splits,
                                         values, weights, int_zeros,
                                         float_zeros, path, feature)
    elif isinstance(inp, ragged_tensor.RaggedTensor):
        self._add_data_for_ragged_tensor(inp, weight, indices_or_row_splits,
                                         values, weights, int_zeros,
                                         float_zeros, path, feature)
    else:
        raise ValueError("Input {} is of unknown type {}. Please only pass "
                         "Tensor, SparseTensor or RaggedTensor as input to "
                         "enqueue.".format(path, type(inp)))

exit(tpu_ops.enqueue_tpu_embedding_arbitrary_tensor_batch(
    sample_indices_or_row_splits=indices_or_row_splits,
    embedding_indices=values,
    aggregation_weights=weights,
    mode_override=mode_override,
    device_ordinal=device_ordinal,
    combiners=combiners))
