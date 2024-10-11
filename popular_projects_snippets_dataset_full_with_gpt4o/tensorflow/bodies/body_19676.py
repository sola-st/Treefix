# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    sample_indices: A list of rank 2 Tensors specifying the training example to
      which the corresponding embedding_indices and aggregation_weights values
      belong. It corresponds to sp_ids.indices in embedding_lookup_sparse(). If
      the size of its first dimension is 0, we assume each embedding_indices
      belongs to a different sample. Both int32 and int64 are allowed and will
      be converted to int32 internally.
    embedding_indices: A list of rank 1 Tensors, indices into the embedding
      tables. It corresponds to sp_ids.values in embedding_lookup_sparse(). Both
      int32 and int64 are allowed and will be converted to int32 internally.
    aggregation_weights: A list of rank 1 Tensors containing per training
      example aggregation weights. It corresponds to sp_weights.values in
      embedding_lookup_sparse(). If the size of its first dimension is 0, we
      assume all weights are 1. Both float32 and float64 are allowed and will be
      converted to float32 internally.
    table_ids: A list of integers specifying the identifier of the embedding
      table (offset of TableDescriptor in the TPUEmbeddingConfiguration) to
      lookup the corresponding input. The ith input is looked up using
      table_ids[i]. The size of the table_ids list must be equal to that of
      sample_indices, embedding_indices and aggregation_weights.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    max_sequence_lengths: A list of integers, the size of which is equal to
      sample_indices. If equal to 0, the corresponding feature is considered to
      be a non-sequence feature, If greater than 0, the corresponding feature is
      a sequence feature with the given maximal length. If None, then we assume
      a list of all zeroes.
    num_features: A list of integers, the size of which is equal to
      sample_indices. If non-empty, entries in this list must be at least 1. For
      each batch element, we will take num_features rows of the input tensor for
      embedding lookup. E.g., when sample_indices is empty, the embedding
      indices must be of shape (batch_size*num_features).
    combiners: A list of string scalars, one for each embedding table that
      specify how to normalize the embedding activations after weighted
      summation. Supported combiners are 'mean', 'sum', or 'sqrtn'. It is
      invalid to have the sum of the weights be 0 for 'mean' or the sum of the
      squared weights be 0 for 'sqrtn'. If combiners isn't passed, the default
      is to use 'sum' for all tables (optional).
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'train', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingSparseTensorBatch operation.
  """
if mode_override is None:
    mode_override = "unspecified"
exit(gen_tpu_ops.enqueue_tpu_embedding_sparse_tensor_batch(
    sample_indices=sample_indices,
    embedding_indices=embedding_indices,
    aggregation_weights=aggregation_weights,
    table_ids=table_ids,
    device_ordinal=device_ordinal,
    max_sequence_lengths=max_sequence_lengths,
    combiners=combiners,
    mode_override=mode_override,
    num_features=num_features,
    name=name))
