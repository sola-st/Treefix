# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with context.eager_mode():
    save_dir = self._get_test_dir("max_to_keep_eager")

    v = variable_scope.variable(10.0, name="v")
    save = saver_module.Saver({"v": v}, max_to_keep=2)
    self.evaluate(variables.global_variables_initializer())
    if not context.executing_eagerly():
        self.assertEqual([], save.last_checkpoints)

    s1 = save.save(None, os.path.join(save_dir, "s1"))
    self.assertEqual([s1], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertCheckpointState(
        model_checkpoint_path=s1,
        all_model_checkpoint_paths=[s1],
        save_dir=save_dir)

    s2 = save.save(None, os.path.join(save_dir, "s2"))
    self.assertEqual([s1, s2], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertCheckpointState(
        model_checkpoint_path=s2,
        all_model_checkpoint_paths=[s1, s2],
        save_dir=save_dir)

    s3 = save.save(None, os.path.join(save_dir, "s3"))
    self.assertEqual([s2, s3], save.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(checkpoint_management.checkpoint_exists(s3))
    self.assertCheckpointState(
        model_checkpoint_path=s3,
        all_model_checkpoint_paths=[s2, s3],
        save_dir=save_dir)

    # Create a second helper, identical to the first.
    save2 = saver_module.Saver({"v": v}, max_to_keep=2)
    save2.set_last_checkpoints(save.last_checkpoints)

    # Exercise the first helper.

    # Adding s2 again (old s2 is removed first, then new s2 appended)
    s2 = save.save(None, os.path.join(save_dir, "s2"))
    self.assertEqual([s3, s2], save.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(checkpoint_management.checkpoint_exists(s3))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertCheckpointState(
        model_checkpoint_path=s2,
        all_model_checkpoint_paths=[s3, s2],
        save_dir=save_dir)

    # Adding s1 (s3 should now be deleted as oldest in list)
    s1 = save.save(None, os.path.join(save_dir, "s1"))
    self.assertEqual([s2, s1], save.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertCheckpointState(
        model_checkpoint_path=s1,
        all_model_checkpoint_paths=[s2, s1],
        save_dir=save_dir)

    s2 = save2.save(None, os.path.join(save_dir, "s2"))
    self.assertEqual([s3, s2], save2.last_checkpoints)
    # Created by the first helper.
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    # Deleted by the first helper.
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
