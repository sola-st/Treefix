# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_dir = self._get_test_dir("no_max_to_keep")
save_dir2 = self._get_test_dir("max_to_keep_0")

with self.cached_session() as sess:
    v = variables.VariableV1(10.0, name="v")
    self.evaluate(variables.global_variables_initializer())

    # Test max_to_keep being None.
    save = saver_module.Saver({"v": v}, max_to_keep=None)
    self.assertEqual([], save.last_checkpoints)
    s1 = save.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    s2 = save.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))

    # Test max_to_keep being 0.
    save2 = saver_module.Saver({"v": v}, max_to_keep=0)
    self.assertEqual([], save2.last_checkpoints)
    s1 = save2.save(sess, os.path.join(save_dir2, "s1"))
    self.assertEqual([], save2.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    s2 = save2.save(sess, os.path.join(save_dir2, "s2"))
    self.assertEqual([], save2.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
