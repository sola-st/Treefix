# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
indices = np.array(indices, dtype=np.int32)
batch_size_index = np.repeat(
    np.arange(self.data_batch_size), len(indices)).reshape(-1, 1)
repeated_indices = np.tile(indices, (self.data_batch_size, 1))
exit(np.concatenate([batch_size_index, repeated_indices], axis=1))
