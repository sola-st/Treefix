# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with context.eager_mode():
    save_dir = self._get_test_dir("recover_last_checkpoints")

    v = variable_scope.variable(10.0, name="v")
    save = saver_module.Saver({"v": v}, max_to_keep=10)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual([], save.last_checkpoints)

    s1 = save.save(None, os.path.join(save_dir, "ckpt-1"))
    s2 = save.save(None, os.path.join(save_dir, "ckpt-2"))
    s3 = save.save(None, os.path.join(save_dir, "ckpt-3"))
    self.assertEqual([s1, s2, s3], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(checkpoint_management.checkpoint_exists(s3))
    self.assertCheckpointState(
        model_checkpoint_path=s3,
        all_model_checkpoint_paths=[s1, s2, s3],
        save_dir=save_dir)

    # Create another saver and recover last checkpoints.
    save2 = saver_module.Saver({"v": v}, max_to_keep=10)
    self.assertEqual([], save2.last_checkpoints)
    save2.recover_last_checkpoints([s1, s2, s3])
    self.assertEqual([s1, s2, s3], save2.last_checkpoints)

    # Remove a checkpoint and check that last checkpoints are
    # restored correctly.
    for fname in gfile.Glob("{}*".format(s1)):
        gfile.Remove(fname)
    self.assertFalse(checkpoint_management.checkpoint_exists(s1))

    # Create another saver and recover last checkpoints. The removed
    # checkpoint would be correctly omitted.
    save3 = saver_module.Saver({"v": v}, max_to_keep=10)
    self.assertEqual([], save3.last_checkpoints)
    save3.recover_last_checkpoints([s1, s2, s3])
    self.assertEqual([s2, s3], save3.last_checkpoints)
    s4 = save3.save(None, os.path.join(save_dir, "ckpt-4"))
    self.assertCheckpointState(
        model_checkpoint_path=s4,
        all_model_checkpoint_paths=[s2, s3, s4],
        save_dir=save_dir)
