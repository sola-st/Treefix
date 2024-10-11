# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session() as sess:
    v0 = variable_scope.get_variable(
        "v0", [1], initializer=init_ops.constant_initializer(0))
    with ops.control_dependencies([v0.value()]):
        v1 = variable_scope.get_variable(
            "v1", [1], initializer=init_ops.constant_initializer(1))
        add = v1 + v0
    # v0 should be uninitialized.
    with self.assertRaisesRegex(errors.OpError, "uninitialized"):
        self.evaluate(v0)
    # We should be able to initialize and run v1 without initializing
    # v0, even if the variable was created with a control dep on v0.
    self.evaluate(v1.initializer)
    self.assertEqual(1, self.evaluate(v1))
    # v0 should still be uninitialized.
    with self.assertRaisesRegex(errors.OpError, "uninitialized"):
        self.evaluate(v0)
    with self.assertRaisesRegex(errors.OpError, "uninitialized"):
        self.evaluate(add)
    # If we initialize v0 we should be able to run 'add'.
    self.evaluate(v0.initializer)
    self.evaluate(add)
