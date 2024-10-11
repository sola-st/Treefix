# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
embedding_table = np.copy(embedding_table_before)
config = optimizer.get_config()
accumulator = (
    config['initial_accumulator_value'] + np.sum(gradients, axis=0)**2)
embedding_table -= (
    config['learning_rate'] * np.sum(gradients, axis=0) /
    np.sqrt(accumulator))
self.assertAllClose(
    self._get_variable(variables['parameters']).numpy(), embedding_table)
self.assertAllClose(
    self._get_variable(variables['accumulators']).numpy(), accumulator)
