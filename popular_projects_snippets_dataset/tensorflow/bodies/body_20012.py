# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Data to be enqueued through generate_enqueue_ops().

    Args:
      embedding_indices: A rank 1 Tensor, indices into the embedding tables. It
        corresponds to sp_ids.values in embedding_lookup_sparse(). Both int32
        and int64 are allowed and will be converted to int32 internally.
      sample_indices: A rank 2 Tensor specifying the training example to which
        the corresponding embedding_indices and aggregation_weights values
        belong. It corresponds to sp_ids.indices in embedding_lookup_sparse().
        If it is None, we assume each embedding_indices belongs to a different
        sample. Both int32 and int64 are allowed and will be converted to int32
        internally.
      aggregation_weights: A rank 1 Tensor containing aggregation weights. It
        corresponds to sp_weights.values in embedding_lookup_sparse(). If it is
        None, we assume all weights are 1. Both float32 and float64 are allowed
        and will be converted to float32 internally.

    Returns:
      An EnqueueData tuple.

    """
exit(super().__new__(cls, embedding_indices, sample_indices,
                       aggregation_weights))
