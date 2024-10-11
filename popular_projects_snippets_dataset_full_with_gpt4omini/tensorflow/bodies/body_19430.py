# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
embedding_table = np.copy(embedding_table_before)
config = optimizer.get_config()
g = np.sum(gradients, axis=0)
v = g**2 * (1 - config['beta_2'])
m = g * (1 - config['beta_1'])
epsilon = config['epsilon']
lr_modifier = np.sqrt(1 - config['beta_2']) / (1 - config['beta_1'])
embedding_table -= (
    m * config['learning_rate'] * lr_modifier / (np.sqrt(v) + epsilon))
self.assertAllClose(
    self._get_variable(variables['parameters']).numpy(),
    embedding_table,
    rtol=1e-3)
self.assertAllClose(
    self._get_variable(variables['momenta']).numpy(), m, rtol=1e-4)
self.assertAllClose(
    self._get_variable(variables['velocities']).numpy(), v, rtol=1e-4)
