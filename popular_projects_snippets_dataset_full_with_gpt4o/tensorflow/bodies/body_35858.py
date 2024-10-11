# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with test_util.use_gpu():
    var = gen_state_ops.temporary_variable([1, 2], dtypes.float32)
    val1 = gen_state_ops.destroy_temporary_variable(var, var_name="dup")
    val2 = gen_state_ops.destroy_temporary_variable(var, var_name="dup")
    final = val1 + val2
    with self.assertRaises(errors.NotFoundError):
        self.evaluate(final)
