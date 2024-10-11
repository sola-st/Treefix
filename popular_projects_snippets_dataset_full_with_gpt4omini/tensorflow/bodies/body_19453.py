# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
embedding_table = np.copy(embedding_table_before)
accumulator = np.zeros(self._get_variable(variable['accumulators']).shape)
momenta = np.zeros(self._get_variable(variable['momenta']).shape)
gradients = np.sum(gradients, axis=0)
if optimizer.beta2 == 1.0:
    accumulator += gradients**2
else:
    accumulator = optimizer.beta2 * accumulator + (
        1 - optimizer.beta2) * gradients**2
accumulator_power = np.power(accumulator + optimizer.epsilon,
                             -1.0 / optimizer.exponent)
momenta = optimizer.momentum * momenta + gradients * accumulator_power
if optimizer.use_nesterov:
    update = optimizer.momentum * momenta + gradients * accumulator_power
else:
    update = momenta
embedding_table -= optimizer.learning_rate * update
self.assertAllClose(
    self._get_variable(variable['parameters']).numpy(),
    embedding_table,
    rtol=1e-3)
self.assertAllClose(
    self._get_variable(variable['accumulators']).numpy(),
    accumulator,
    rtol=1e-3)
self.assertAllClose(
    self._get_variable(variable['momenta']).numpy(), momenta, rtol=1e-3)
