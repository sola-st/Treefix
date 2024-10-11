# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
# Sanity check that the slices uses a different seed when using a random
# initializer function.
with self.cached_session():
    var0, var1 = partitioned_variables.create_partitioned_variables(
        [20, 12], [1, 2], init_ops.random_uniform_initializer())
    self.evaluate(variables.global_variables_initializer())
    val0, val1 = self.evaluate(var0).flatten(), self.evaluate(var1).flatten()
    self.assertTrue(np.linalg.norm(val0 - val1) > 1e-6)
# Negative test that proves that slices have the same values if
# the random initializer uses a seed.
with self.cached_session():
    var0, var1 = partitioned_variables.create_partitioned_variables(
        [20, 12], [1, 2], init_ops.random_uniform_initializer(seed=201))
    self.evaluate(variables.global_variables_initializer())
    val0, val1 = self.evaluate(var0).flatten(), self.evaluate(var1).flatten()
    self.assertAllClose(val0, val1)
