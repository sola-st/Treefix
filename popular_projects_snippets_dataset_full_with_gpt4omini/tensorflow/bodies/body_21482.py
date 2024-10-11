# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
"""Save, copy checkpoint dir and restore from copied dir.

    This only works for save_relative_paths=True.
    """
save_dir1 = os.path.join(self.get_temp_dir(), "save_dir1")
os.mkdir(save_dir1)
save_path1 = os.path.join(save_dir1, "save_copy_restore")

# train.Saver is V1 only API.
with ops_lib.Graph().as_default():
    # Build a graph with 2 parameter nodes, and Save and
    # Restore nodes for them.
    v0 = variables.VariableV1(10.0, name="v0")
    v1 = variables.VariableV1(20.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    v2_init = v2.insert("k1", 30.0)
    save = saver_module.Saver(
        var_list={
            "v0": v0,
            "v1": v1,
            "v2": v2.saveable
        },
        restore_sequentially=True,
        save_relative_paths=True)
    init_all_op = [variables.global_variables_initializer(), v2_init]

    with self.cached_session() as sess:
        # Initialize all variables
        self.evaluate(init_all_op)

        # Check that the parameter nodes have been initialized.
        self.assertEqual(10.0, self.evaluate(v0))
        self.assertEqual(20.0, self.evaluate(v1))
        self.assertEqual(b"k1", self.evaluate(v2.keys()))
        self.assertEqual(30.0, self.evaluate(v2.values()))

        # Save the initialized values in the file at "save_path"
        val = save.save(sess, save_path1)
        self.assertIsInstance(val, str)
        self.assertEqual(save_path1, val)

    self.assertEqual(
        checkpoint_management.latest_checkpoint(save_dir1), save_path1)
    save_dir2 = os.path.join(self.get_temp_dir(), "save_dir2")
    os.renames(save_dir1, save_dir2)
    save_path2 = os.path.join(save_dir2, "save_copy_restore")
    self.assertEqual(
        checkpoint_management.latest_checkpoint(save_dir2), save_path2)

    # Start a second session.  In that session the parameter nodes
    # have not been initialized either.
    with self.cached_session() as sess:
        v0 = variables.VariableV1(-1.0, name="v0")
        v1 = variables.VariableV1(-1.0, name="v1")
        v2 = saver_test_utils.CheckpointedOp(name="v2")
        save = saver_module.Saver({"v0": v0, "v1": v1, "v2": v2.saveable})

        # Assert that the variables are not initialized.
        self.assertEqual(
            len(variables.report_uninitialized_variables().eval()), 2)
        self.assertEqual(0, len(self.evaluate(v2.keys())))
        self.assertEqual(0, len(self.evaluate(v2.values())))

        # Restore the saved values in the parameter nodes.
        save.restore(sess, save_path2)
        # Check that the parameter nodes have been restored.
        self.assertEqual(10.0, self.evaluate(v0))
        self.assertEqual(20.0, self.evaluate(v1))
        self.assertEqual(b"k1", self.evaluate(v2.keys()))
        self.assertEqual(30.0, self.evaluate(v2.values()))
