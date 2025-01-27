# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd = variables.Variable(random_ops.random_uniform([200, 40]))
    vs = partitioned_variables.create_partitioned_variables(
        rnd.get_shape(), [1, 10], rnd.initialized_value())
    self.evaluate(variables.global_variables_initializer())
    val = array_ops.concat(vs, 1)
    rnd = self.evaluate(rnd)
    self.assertAllClose(rnd, val)
    self.assertEqual([dtypes.float32] * 10, [v.dtype.base_dtype for v in vs])
    self._TestSaveSpec(vs, [
        "200 40 0,200:0,4", "200 40 0,200:4,4", "200 40 0,200:8,4",
        "200 40 0,200:12,4", "200 40 0,200:16,4", "200 40 0,200:20,4",
        "200 40 0,200:24,4", "200 40 0,200:28,4", "200 40 0,200:32,4",
        "200 40 0,200:36,4"
    ])
