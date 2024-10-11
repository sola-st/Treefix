# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1, v2, v3, v4 = _create_checkpoints(session, checkpoint_dir)

# New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        with variable_scope.variable_scope("some_scope"):
            my1 = variable_scope.get_variable("var1", [1, 10])
            my2 = variable_scope.get_variable("var2", [10, 10])
            my3 = variable_scope.get_variable("var3", [100, 100])
            with variable_scope.variable_scope("useful_scope"):
                my4 = variable_scope.get_variable("var4", [9, 9])

        checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                              {"/": "some_scope/",})

        session.run(variables.global_variables_initializer())
        self.assertAllEqual(my1.eval(session), v1)
        self.assertAllEqual(my2.eval(session), v2)
        self.assertAllEqual(my3.eval(session), v3)
        self.assertAllEqual(my4.eval(session), v4)
