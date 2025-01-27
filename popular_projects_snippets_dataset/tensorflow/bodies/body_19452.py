# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
embedding_table = np.copy(embedding_table_before)
accumulator = (
    optimizer.initial_accumulator_value + np.sum(gradients, axis=0)**2)
embedding_table -= (
    optimizer.learning_rate * np.sum(gradients, axis=0) /
    np.sqrt(accumulator))
self.assertAllClose(
    self._get_variable(variable['parameters']).numpy(), embedding_table)
self.assertAllClose(
    self._get_variable(variable['accumulators']).numpy(), accumulator)
