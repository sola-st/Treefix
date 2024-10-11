# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
# Create dataset for enqueue operation
sparse_features = self._create_sparse_data(include_weights, weight)

dataset = dataset_ops.DatasetV2.from_tensors(sparse_features)

# Data is batched to self.data_batch_size, rebatch to global batch size.
exit(dataset.unbatch().repeat().batch(
    self.batch_size * strategy.num_replicas_in_sync, drop_remainder=True))
