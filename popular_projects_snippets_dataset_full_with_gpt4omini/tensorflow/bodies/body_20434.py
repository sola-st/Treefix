# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""Uses XLA's dynamic slice operations to perform embedding lookups.

  From third_party/cloud_tpu/models/movielens/tpu_embedding.py

  Args:
    params: Tensor of embedding table. Rank 2 (table_size x embedding dim)
    values_and_values_mask: is a two-tuple that contains: values - Tensor of
      embedding indices. Rank 2 (batch x n_indices) values_mask - Tensor of mask
      / weights. Rank 2 (batch x n_indices)
    combiner: The combiner to use for the embedding lookup. Currently supports
      'sum' and 'mean'.
    name: Optional name scope for created ops

  Returns:
    Rank 2 tensor of aggregated (per batch element) embedding vectors.

  Raises:
    ValueError: Combiner is not supported.
  """
values, values_mask = values_and_values_mask  # unpack the two-tuple
with ops.name_scope(name):
    _, embedding_dimension = params.get_shape().as_list()
    n_batch, n_indices_padded = values.get_shape().as_list()
    if not n_batch:
        n_batch = -1

    emb_lookup = array_ops.reshape(
        embedding_ops.embedding_lookup(
            params, array_ops.reshape(values, [n_batch, n_indices_padded])),
        [n_batch, n_indices_padded, embedding_dimension])

    values_mask_broadcast = array_ops.reshape(values_mask,
                                              [n_batch, n_indices_padded, 1])
    aggregate_emb = math_ops.reduce_sum(
        emb_lookup * values_mask_broadcast, axis=1)
    if combiner == 'sum':
        exit(aggregate_emb)
    elif combiner == 'mean':
        # In the case we have an empty row, both aggregate_emb and
        # math_ops.reduce_sum(values_mask_broadcast, axis=1) will be 0. Thus,
        # we can take max it with a non-zero value to prevent NaNs. Note that
        # math_ops.reduce_sum(values_mask_broadcast, axis=1) will have integer
        # values so 1.0 is the smallest value.
        exit(aggregate_emb / math_ops.maximum(
            math_ops.reduce_sum(values_mask_broadcast, axis=1), 1.0))
    else:
        raise ValueError('Dense TPU Embedding does not support combiner '
                         'other than sum and mean.')
