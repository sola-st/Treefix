# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    with variable_scope.variable_scope("foo"):
        var = variable_scope.get_variable("x", shape=[1, 1],
                                          dtype=dtypes.float32)
        with self.assertRaisesRegex(ValueError,
                                    "shape.*and.*are incompatible"):
            assign = var.assign(np.zeros(shape=[2, 2]))
            self.evaluate(assign)
