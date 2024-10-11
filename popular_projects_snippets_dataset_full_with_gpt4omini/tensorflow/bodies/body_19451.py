# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
embedding_table = np.copy(embedding_table_before)
embedding_table -= optimizer.learning_rate * np.sum(gradients, axis=0)
self.assertAllClose(
    self._get_variable(variables['parameters']).numpy(), embedding_table)
