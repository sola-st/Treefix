# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Data to be enqueued through generate_enqueue_ops().

    Args:
      embedding_indices: A rank 1 Tensor, indices into the embedding tables. It
        corresponds to ids.values in embedding_lookup(), when ids is a
        RaggedTensor. Both int32 and int64 are allowed and will be converted to
        int32 internally.
      row_splits: A rank 1 Tensor specifying the length of  the break points for
        splitting embedding_indices and aggregation_weights. It corresponds to
        ids.row_splits in embedding_lookup(), when ids is a RaggedTensor. Both
        int32 and int64 are allowed and will be converted to int32 internally.
      aggregation_weights: A rank 1 Tensor containing per training example
        aggregation weights. It corresponds to the values field of a
        RaggedTensor with the same row_splits as ids in embedding_lookup(), when
        ids is a RaggedTensor.

    Returns:
      An RaggedEnqueueData tuple.

    """
exit(super().__new__(cls, embedding_indices, row_splits,
                       aggregation_weights))
