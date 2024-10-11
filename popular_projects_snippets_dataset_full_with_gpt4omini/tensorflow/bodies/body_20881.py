# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1, _, _, _ = _create_checkpoints(session, checkpoint_dir)

# New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        with variable_scope.variable_scope(
            "some_scope", initializer=init_ops.zeros_initializer()):
            my1 = variable_scope.get_variable("my1", [1, 10])

        before = my1.initialized_value()

        checkpoint_utils.init_from_checkpoint(checkpoint_dir, {"var1": my1})

        after = my1.initialized_value()

        self.assertAllEqual(session.run(before), [[0.0] * 10])
        self.assertAllEqual(session.run(after), v1)

        session.run(variables.global_variables_initializer())

        self.assertAllEqual(session.run(my1), v1)
        self.assertAllEqual(session.run(my1.initialized_value()), v1)
        self.assertAllClose(session.run(before), v1)
        self.assertAllClose(session.run(after), v1)
        with self.assertRaises(AssertionError):
            self.assertAllClose(v1, [[0.0] * 10])
