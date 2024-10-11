# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
for variable_op in [
    variables.Variable, resource_variable_ops.ResourceVariable
]:
    save_path = os.path.join(self.get_temp_dir(), "basic_save_restore")

    # Build the first session.
    with self.session(graph=ops_lib.Graph()) as sess:
        v0 = variable_op(10.0, name="v0", dtype=dtypes.float32)

        if not context.executing_eagerly():
            self.evaluate([variables.global_variables_initializer()])

        save = saver_module.Saver({"v0": v0})
        save.save(sess, save_path)

    # Start a second session.
    with self.session(graph=ops_lib.Graph()) as sess:
        v0_wrong_dtype = variable_op(1, name="v0", dtype=dtypes.int32)
        # Restore the saved value with different dtype
        # in the parameter nodes.
        save = saver_module.Saver({"v0": v0_wrong_dtype})
        with self.assertRaisesRegex(errors.InvalidArgumentError,
                                    "original dtype"):
            save.restore(sess, save_path)
