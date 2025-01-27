# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
file_io.write_string_to_file(
    os.path.join(self.get_temp_dir(), "actually_a_file"), "")
paths = [
    os.path.join(self.get_temp_dir(), "nonexisting_dir/path"),
    os.path.join(self.get_temp_dir(), "other_nonexisting_dir/path1/path2"),
    os.path.join(self.get_temp_dir(), "actually_a_file/path"),
]

for save_path in paths:
    # Build a graph with 2 parameter nodes, and Save and
    # Restore nodes for them.
    v0 = variables.VariableV1(10.0, name="v0")
    v1 = variables.VariableV1(20.0, name="v1")
    save = saver_module.Saver({"v0": v0, "v1": v1}, restore_sequentially=True)
    init_all_op = variables.global_variables_initializer()

    # In the case where the parent directory doesn't exist, whether or not the
    # save succeeds or fails is implementation dependent.  Therefore we allow
    # both cases.
    try:
        with self.cached_session() as sess:
            # Initialize all variables
            self.evaluate(init_all_op)

            # Check that the parameter nodes have been initialized.
            self.assertEqual(10.0, self.evaluate(v0))
            self.assertEqual(20.0, self.evaluate(v1))

            # Save the graph.
            save.save(sess, save_path)

        with self.cached_session() as sess:
            # Restore the saved values in the parameter nodes.
            save.restore(sess, save_path)
            # Check that the parameter nodes have been restored.
            self.assertEqual(10.0, self.evaluate(v0))
            self.assertEqual(20.0, self.evaluate(v1))
    except ValueError as exc:
        error_msg_template = "Parent directory of {} doesn't exist, can't save."
        self.assertEqual(error_msg_template.format(save_path), str(exc))
