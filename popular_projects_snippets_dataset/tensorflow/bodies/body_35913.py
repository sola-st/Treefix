# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with context.eager_mode():
    container = variable_scope.EagerVariableStore()
    x = constant_op.constant([[2.0]])
    with container.as_default():
        y = core_layers.dense(x, 1, name="my_dense",
                              kernel_initializer=init_ops.ones_initializer())
    self.assertAllEqual(y, [[2.0]])
    self.assertEqual(len(container.variables()), 2)
    # Recreate the layer to test reuse.
    with container.as_default():
        core_layers.dense(x, 1, name="my_dense",
                          kernel_initializer=init_ops.ones_initializer())
    self.assertEqual(len(container.variables()), 2)
