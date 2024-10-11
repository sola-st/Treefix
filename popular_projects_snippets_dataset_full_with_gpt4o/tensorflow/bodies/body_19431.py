# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
embedding_table = np.copy(embedding_table_before)
config = optimizer.get_config()
neg_lr_p = -config['learning_rate_power']
accumulator = (
    config['initial_accumulator_value'] + np.sum(gradients, axis=0)**2)
sigma = (accumulator**neg_lr_p - config['initial_accumulator_value']**
         neg_lr_p) / config['learning_rate']
linear = np.sum(gradients, axis=0) - sigma * embedding_table
quadratic = accumulator**neg_lr_p / config['learning_rate']
embedding_table = -linear / quadratic
actual_parameters = self._get_variable(variables['parameters']).numpy()
# For entries where `linear` == 0, it is not worth comparing since the
# initial values have not been touched yet and they will not agree with what
# the actual values should be.
actual_parameters *= (linear != 0.0)
# FTRL has a bit more precision diff on parameters.
self.assertAllClose(actual_parameters, embedding_table, rtol=5e-5)
self.assertAllClose(
    self._get_variable(variables['linears']).numpy(), linear, rtol=5e-4)
self.assertAllClose(
    self._get_variable(variables['accumulators']).numpy(), accumulator)
