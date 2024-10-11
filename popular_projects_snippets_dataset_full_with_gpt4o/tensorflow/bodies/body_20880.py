# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1, v2, v3, v4 = _create_checkpoints(session, checkpoint_dir)

# New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        with variable_scope.variable_scope("some_scope"):
            my1 = variable_scope.get_variable("my1", [1, 10])
            with variable_scope.variable_scope("some_other_scope"):
                my2 = variable_scope.get_variable("my2", [10, 10])
                with variable_scope.variable_scope("other_useful_scope"):
                    my4 = variable_scope.get_variable("var4", [9, 9])
        my3 = variable_scope.get_variable("my3", [100, 100])
        my3b = variable_scope.get_variable("my3b", [100, 100])

        checkpoint_utils.init_from_checkpoint(checkpoint_dir, {
            "var1": "some_scope/my1",
            "useful_scope/": "some_scope/some_other_scope/other_useful_scope/",
        })
        checkpoint_utils.init_from_checkpoint(checkpoint_dir, [
            ("var2", "some_scope/some_other_scope/my2"),
            ("var3", my3),
            ("var3", my3b),
        ])

        session.run(variables.global_variables_initializer())
        self.assertAllEqual(my1.eval(session), v1)
        self.assertAllEqual(my2.eval(session), v2)
        self.assertAllEqual(my3.eval(session), v3)
        self.assertAllEqual(my3b.eval(session), v3)
        self.assertAllEqual(my4.eval(session), v4)

        # Check that tensors are not explicitly in the graph.
        self.assertLess(len(str(session.graph.as_graph_def())), 32000)
