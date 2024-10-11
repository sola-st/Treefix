# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with test_util.use_gpu():
    var1 = gen_state_ops.temporary_variable([1, 2],
                                            dtypes.float32,
                                            var_name="dup")
    var1 = state_ops.assign(var1, [[1.0, 2.0]])
    var2 = gen_state_ops.temporary_variable([1, 2],
                                            dtypes.float32,
                                            var_name="dup")
    var2 = state_ops.assign(var2, [[3.0, 4.0]])
    final = var1 + var2
    with self.assertRaises(errors.AlreadyExistsError):
        self.evaluate(final)
