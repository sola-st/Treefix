# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with test_util.use_gpu():
    abc = variable_scope.get_variable(
        "abc",
        shape=[1],
        initializer=init_ops.ones_initializer(),
        use_resource=True)

    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(
        self.evaluate(
            resource_variable_ops.var_is_initialized_op(abc.handle)),
        True)
