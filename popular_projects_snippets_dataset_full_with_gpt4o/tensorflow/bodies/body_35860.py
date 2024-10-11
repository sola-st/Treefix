# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with test_util.use_gpu():
    var1 = gen_state_ops.temporary_variable([1, 2],
                                            dtypes.float32,
                                            var_name="var1")
    var2 = gen_state_ops.temporary_variable([1, 2],
                                            dtypes.float32,
                                            var_name="var2")
    final = var1 + var2
    self.evaluate(final)
