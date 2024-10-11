# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "non_reshape")

with self.session(graph=ops_lib.Graph()) as sess:
    # Build a graph with 2 parameter nodes, and Save and
    # Restore nodes for them.
    v0 = variable_op(10.0, name="v0")
    v1 = variable_op(20.0, name="v1")
    save = saver_module.Saver({"save_prefix/v0": v0, "save_prefix/v1": v1})
    self.evaluate(variables.global_variables_initializer())

    # Check that the parameter nodes have been initialized.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))

    # Save the initialized values in the file at "save_path"
    # Use a variable name map to set the saved tensor names
    val = save.save(sess, save_path)
    self.assertIsInstance(val, str)
    self.assertEqual(save_path, val)

    # Verify that the original names are not in the Saved file
    save = saver_module.Saver({"v0": v0, "v1": v1})
    with self.assertRaisesOpError("not found in checkpoint"):
        save.restore(sess, save_path)

    # Verify that the mapped names are present in the Saved file and can be
    # Restored using remapped names.
with self.session(graph=ops_lib.Graph()) as sess:
    v0 = variable_op(-1.0, name="v0")
    v1 = variable_op(-1.0, name="v1")

    if not context.executing_eagerly():
        with self.assertRaisesOpError("uninitialized"):
            self.evaluate(v0)
        with self.assertRaisesOpError("uninitialized"):
            self.evaluate(v1)

    save = saver_module.Saver({"save_prefix/v0": v0, "save_prefix/v1": v1})
    save.restore(sess, save_path)

    # Check that the parameter nodes have been restored.
    if not context.executing_eagerly():
        self.assertEqual(10.0, self.evaluate(v0))
        self.assertEqual(20.0, self.evaluate(v1))

    # Add a prefix to the node names in the current graph and Restore using
    # remapped names.
with self.session(graph=ops_lib.Graph()) as sess:
    v0 = variable_op(-1.0, name="restore_prefix/v0")
    v1 = variable_op(-1.0, name="restore_prefix/v1")

    if not context.executing_eagerly():
        with self.assertRaisesOpError("uninitialized"):
            self.evaluate(v0)
        with self.assertRaisesOpError("uninitialized"):
            self.evaluate(v1)

      # Restore the saved values in the parameter nodes.
    save = saver_module.Saver({"save_prefix/v0": v0, "save_prefix/v1": v1})
    save.restore(sess, save_path)

    # Check that the parameter nodes have been restored.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))
