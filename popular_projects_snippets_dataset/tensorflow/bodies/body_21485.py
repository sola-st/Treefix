# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "int64")

with self.cached_session() as sess:
    # Build a graph with 1 node, and save and restore for them.
    v = variables.VariableV1(np.int64(15), name="v")
    save = saver_module.Saver({"v": v}, restore_sequentially=True)
    self.evaluate(variables.global_variables_initializer())

    # Save the initialized values in the file at "save_path"
    val = save.save(sess, save_path)
    self.assertIsInstance(val, str)
    self.assertEqual(save_path, val)

    with self.cached_session() as sess:
        v = variables.VariableV1(np.int64(-1), name="v")
        save = saver_module.Saver({"v": v})

    with self.assertRaisesWithPredicateMatch(
        errors_impl.OpError, lambda e: "uninitialized value v" in e.message):
        self.evaluate(v)

    # Restore the saved values in the parameter nodes.
    save.restore(sess, save_path)
    # Check that the parameter nodes have been restored.
    self.assertEqual(np.int64(15), self.evaluate(v))
