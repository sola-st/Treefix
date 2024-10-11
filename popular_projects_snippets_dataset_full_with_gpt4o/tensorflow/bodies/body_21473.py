# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "basic_save_restore")

with self.session(graph=ops_lib.Graph()) as sess:
    # Build a graph with 2 parameter nodes, and Save and
    # Restore nodes for them.
    v0 = variable_op(10.0, name="v0")
    v1 = variable_op(20.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    v2_init = v2.insert("k1", 30.0)

    # Initialize all variables
    if not context.executing_eagerly():
        self.evaluate([variables.global_variables_initializer(), v2_init])

        # Check that the parameter nodes have been initialized.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))
    self.assertEqual(b"k1", self.evaluate(v2.keys()))
    self.assertEqual(30.0, self.evaluate(v2.values()))

    # Save the initialized values in the file at "save_path"
    save = saver_module.Saver(
        {
            "v0": v0,
            "v1": v1,
            "v2": v2.saveable
        }, restore_sequentially=True)
    val = save.save(sess, save_path)
    self.assertIsInstance(val, str)
    self.assertEqual(save_path, val)

# Start a second session.  In that session the parameter nodes
# have not been initialized either.
with self.session(graph=ops_lib.Graph()) as sess:
    v0 = variable_op(-1.0, name="v0")
    v1 = variable_op(-1.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")

    # Assert that the variables are not initialized.
    if not context.executing_eagerly():
        self.assertEqual(
            len(variables.report_uninitialized_variables().eval()), 2)
        self.assertEqual(0, len(self.evaluate(v2.keys())))
        self.assertEqual(0, len(self.evaluate(v2.values())))
    # Restore the saved values in the parameter nodes.
    save = saver_module.Saver({"v0": v0, "v1": v1, "v2": v2.saveable})
    save.restore(sess, save_path)
    # Check that the parameter nodes have been restored.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))
    self.assertEqual(b"k1", self.evaluate(v2.keys()))
    self.assertEqual(30.0, self.evaluate(v2.values()))

# Build another graph with 2 nodes, initialized
# differently, and a Restore node for them.
with self.session(graph=ops_lib.Graph()) as sess:
    v0_2 = variable_op(1000.0, name="v0")
    v1_2 = variable_op(2000.0, name="v1")
    v2_2 = saver_test_utils.CheckpointedOp(name="v2")
    v2_init = v2_2.insert("k1000", 3000.0)

    # Check that the parameter nodes have been initialized.
    if not context.executing_eagerly():
        init_all_op = [variables.global_variables_initializer(), v2_init]
        self.evaluate(init_all_op)
        # TODO(xpan): Why _mutable_hash_table_v2 doesn't create empty
        # table as it claims in eager mode?
        self.assertEqual(b"k1000", self.evaluate(v2_2.keys()))
        self.assertEqual(3000.0, self.evaluate(v2_2.values()))
    self.assertEqual(1000.0, self.evaluate(v0_2))
    self.assertEqual(2000.0, self.evaluate(v1_2))

    # Restore the values saved earlier in the parameter nodes.
    save2 = saver_module.Saver({"v0": v0_2, "v1": v1_2, "v2": v2_2.saveable})
    save2.restore(sess, save_path)
    # Check that the parameter nodes have been restored.
    self.assertEqual(10.0, self.evaluate(v0_2))
    self.assertEqual(20.0, self.evaluate(v1_2))
    self.assertEqual(b"k1", self.evaluate(v2_2.keys()))
    self.assertEqual(30.0, self.evaluate(v2_2.values()))
