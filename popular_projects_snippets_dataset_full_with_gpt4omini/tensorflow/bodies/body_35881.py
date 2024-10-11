# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd_par = constant_op.constant([1, 2, 3, 4])
    vs = partitioned_variables.create_partitioned_variables([4], [4], rnd_par)
    self.evaluate(variables.global_variables_initializer())
    val = array_ops.concat(vs, 0)
    rnd = self.evaluate(rnd_par)
    self.assertAllClose(rnd, val)
    self.assertEqual([dtypes.int32] * 4, [v.dtype.base_dtype for v in vs])
    self._TestSaveSpec(vs, ["4 0,1", "4 1,1", "4 2,1", "4 3,1"])
