# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
# Create dataset for enqueue operation
sparse_features = self._create_sparse_data(include_weights, weight)
ragged_features = nest.map_structure(ragged_tensor.RaggedTensor.from_sparse,
                                     sparse_features)

dataset = dataset_ops.DatasetV2.from_tensors(ragged_features)

# Data is batched to self.data_batch_size, rebatch to global batch size.
exit(dataset.unbatch().repeat().batch(
    self.batch_size * strategy.num_replicas_in_sync, drop_remainder=True))
