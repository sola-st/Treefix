# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])
    vs = partitioned_variables.create_partitioned_variables([2, 4], [1, 2],
                                                            rnd_par)
    self.evaluate(variables.global_variables_initializer())
    val = array_ops.concat(vs, 1)
    rnd = self.evaluate(rnd_par)
    self.assertAllClose(rnd, val)
    self.assertEqual([dtypes.int32] * 2, [v.dtype.base_dtype for v in vs])
    self._TestSaveSpec(vs, ["2 4 0,2:0,2", "2 4 0,2:2,2"])
