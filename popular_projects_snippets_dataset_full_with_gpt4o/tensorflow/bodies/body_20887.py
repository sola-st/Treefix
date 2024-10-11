# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    _, _, _, _ = _create_checkpoints(session, checkpoint_dir)

# New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        with variable_scope.variable_scope("some_scope"):
            _ = variable_scope.get_variable("my1", [10, 10])
            _ = variable_scope.get_variable(
                "my2", [1, 10],
                dtype=dtypes.int64,
                initializer=init_ops.zeros_initializer())

        # No directory.
        with self.assertRaises(errors_impl.OpError):
            checkpoint_utils.init_from_checkpoint("no_dir",
                                                  {"var1": "some_scope/my1"})

        # No variable in checkpoint.
        with self.assertRaises(ValueError):
            checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                                  {"no_var": "some_scope/my1"})

        # No variable in the graph.
        with self.assertRaises(ValueError):
            checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                                  {"var3": "some_scope/no_var"})

        # Shape mismatch.
        with self.assertRaises(ValueError):
            checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                                  {"var1": "some_scope/my1"})

        # Variable 'my1' and 'my2' are missing in given checkpoint scope.
        with self.assertRaises(ValueError):
            checkpoint_utils.init_from_checkpoint(
                checkpoint_dir, {"useful_scope/": "some_scope/"})

        # Mapping is not to scope name.
        with self.assertRaises(ValueError):
            checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                                  {"useful_scope": "some_scope/"})
