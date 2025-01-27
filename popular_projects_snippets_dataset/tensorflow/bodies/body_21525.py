# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_dir = self._get_test_dir("no_meta_graph")

with self.cached_session() as sess:
    v = variables.VariableV1(10.0, name="v")
    save = saver_module.Saver({"v": v})
    self.evaluate(variables.global_variables_initializer())

    s1 = save.save(sess, os.path.join(save_dir, "s1"), write_meta_graph=False)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertFalse(
        gfile.Exists(checkpoint_management.meta_graph_filename(s1)))
