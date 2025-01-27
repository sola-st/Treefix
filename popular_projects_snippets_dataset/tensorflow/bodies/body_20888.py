# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1, _, _, _ = _create_checkpoints(session, checkpoint_dir)

# New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        my1 = resource_variable_ops.ResourceVariable([[0.0] * 10], name="my1")

        with ops.name_scope("init_from_checkpoint"):
            checkpoint_utils.init_from_checkpoint(checkpoint_dir, {"var1": my1})

        # Basic sanity checks:
        session.run(variables.global_variables_initializer())
        self.assertAllEqual(session.run(my1), v1)

ops_in_init_from_checkpoint_scope = [
    op for op in g.get_operations()
    if (op.name.startswith("init_from_checkpoint/") and
        not op.name.startswith("init_from_checkpoint/checkpoint_initializer"
                              ) and
        op.type != "AssignVariableOp" and
        op.type != "Identity")
]
self.assertEqual(ops_in_init_from_checkpoint_scope, [])
