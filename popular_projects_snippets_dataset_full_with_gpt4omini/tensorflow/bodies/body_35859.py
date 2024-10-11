# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with test_util.use_gpu():
    var = gen_state_ops.temporary_variable([1, 2],
                                           dtypes.float32,
                                           var_name="bar")
    final = array_ops.identity(var)
    self.evaluate(final)
