# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
embedding_table = np.copy(embedding_table_before)
g = np.sum(gradients, axis=0)
v = g**2 * (1 - optimizer.beta_2)
m = g * (1 - optimizer.beta_1)
epsilon = optimizer.epsilon
# TPU Embeddings don't have the LR decay factor for Adam.
lr_modifier = 1
embedding_table -= (
    m * optimizer.learning_rate * lr_modifier / (np.sqrt(v) + epsilon))
self.assertAllClose(
    self._get_variable(variable['parameters']).numpy(),
    embedding_table,
    rtol=1e-4)
self.assertAllClose(
    self._get_variable(variable['momenta']).numpy(), m, rtol=1e-4)
self.assertAllClose(
    self._get_variable(variable['velocities']).numpy(), v, rtol=1e-4)
