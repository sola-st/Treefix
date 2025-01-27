# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with test_util.use_gpu():
    var = gen_state_ops.temporary_variable([1, 2],
                                           dtypes.float32,
                                           var_name="foo")
    var = state_ops.assign(var, [[4.0, 5.0]])
    var = state_ops.assign_add(var, [[6.0, 7.0]])
    final = gen_state_ops.destroy_temporary_variable(var, var_name="foo")
    self.assertAllClose([[10.0, 12.0]], self.evaluate(final))
