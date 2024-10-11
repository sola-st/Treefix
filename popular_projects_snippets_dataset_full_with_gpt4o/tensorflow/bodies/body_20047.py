# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Format features for `enqueue_tpu_embedding_arbitrary_tensor_batch()`.

    Args:
      enqueue_datas: a `Dict` of `RaggedEnqueueData` objects for embedding.
      ragged: If True, extract row splits from the data rather than sample
        indices.

    Returns:
      Dict of arguments for `enqueue_tpu_embedding_arbitrary_tensor_batch()`.
    """

kwargs = {
    'sample_indices_or_row_splits': [],
    'embedding_indices': [],
    'aggregation_weights': [],
}
int_zeros = array_ops.zeros((0,), dtype=dtypes.int64)
float_zeros = array_ops.zeros((0,), dtype=dtypes.float32)
for table in self._table_to_features_dict:
    features = self._table_to_features_dict[table]
    for feature in features:
        enqueue_data = enqueue_datas[feature]
        if ragged:
            kwargs['sample_indices_or_row_splits'].append(
                enqueue_data.row_splits if enqueue_data
                .row_splits is not None else int_zeros)
        else:
            if (self._feature_to_config_dict[feature].max_sequence_length > 0 and
                enqueue_data.sample_indices is not None and
                enqueue_data.sample_indices.shape[1] == 2):
                # Pad the sample indices as if the enqueued sparse tensor is rank 2.
                sample_indices = array_ops.pad(
                    enqueue_data.sample_indices, paddings=[[0, 0], [0, 1]])
                kwargs['sample_indices_or_row_splits'].append(sample_indices)
            else:
                # If the sample_indices is rank 1 or not present, treat it as dense
                # tensor.
                if (enqueue_data.sample_indices is None or
                    enqueue_data.sample_indices.shape[1] == 1):
                    kwargs['sample_indices_or_row_splits'].append(int_zeros)
                else:
                    kwargs['sample_indices_or_row_splits'].append(
                        enqueue_data.sample_indices)

        kwargs['aggregation_weights'].append(
            enqueue_data.aggregation_weights if enqueue_data
            .aggregation_weights is not None else float_zeros)

        kwargs['embedding_indices'].append(enqueue_data.embedding_indices)
exit(kwargs)
