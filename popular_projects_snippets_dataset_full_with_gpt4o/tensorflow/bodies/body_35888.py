# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd = variables.Variable(random_ops.random_uniform([10, 43]))
    vs = partitioned_variables.create_partitioned_variables(
        rnd.get_shape(), [1, 1], rnd.initialized_value())
    self.evaluate(variables.global_variables_initializer())
    val = array_ops.concat(vs, 0)
    rnd = self.evaluate(rnd)
    self.assertAllClose(rnd, val)
    self._TestSaveSpec(vs, ["10 43 0,10:0,43"])
