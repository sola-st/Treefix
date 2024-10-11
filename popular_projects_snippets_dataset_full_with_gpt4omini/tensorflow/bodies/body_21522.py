# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_dir = self._get_test_dir("max_to_keep_non_sharded")

# train.Saver is V1 only API.
with ops_lib.Graph().as_default(), self.cached_session() as sess:
    v = variables.VariableV1(10.0, name="v")
    save = saver_module.Saver({"v": v}, max_to_keep=2)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual([], save.last_checkpoints)

    s1 = save.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([s1], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertCheckpointState(
        model_checkpoint_path=s1,
        all_model_checkpoint_paths=[s1],
        save_dir=save_dir)

    s2 = save.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([s1, s2], save.last_checkpoints)
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertCheckpointState(
        model_checkpoint_path=s2,
        all_model_checkpoint_paths=[s1, s2],
        save_dir=save_dir)

    s3 = save.save(sess, os.path.join(save_dir, "s3"))
    self.assertEqual([s2, s3], save.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(checkpoint_management.checkpoint_exists(s3))
    self.assertCheckpointState(
        model_checkpoint_path=s3,
        all_model_checkpoint_paths=[s2, s3],
        save_dir=save_dir)

    # Create a second helper, identical to the first.
    save2 = saver_module.Saver(saver_def=save.as_saver_def())
    save2.set_last_checkpoints(save.last_checkpoints)

    # Create a third helper, with the same configuration but no knowledge of
    # previous checkpoints.
    save3 = saver_module.Saver(saver_def=save.as_saver_def())

    # Exercise the first helper.

    # Adding s2 again (old s2 is removed first, then new s2 appended)
    s2 = save.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([s3, s2], save.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s1))
    self.assertFalse(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s1)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s3))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s3)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s2)))
    self.assertCheckpointState(
        model_checkpoint_path=s2,
        all_model_checkpoint_paths=[s3, s2],
        save_dir=save_dir)

    # Adding s1 (s3 should now be deleted as oldest in list)
    s1 = save.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([s2, s1], save.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
    self.assertFalse(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s3)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s2)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s1)))
    self.assertCheckpointState(
        model_checkpoint_path=s1,
        all_model_checkpoint_paths=[s2, s1],
        save_dir=save_dir)

    # Exercise the second helper.

    # Adding s2 again (old s2 is removed first, then new s2 appended)
    s2 = save2.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([s3, s2], save2.last_checkpoints)
    # Created by the first helper.
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s1)))
    # Deleted by the first helper.
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
    self.assertFalse(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s3)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s2)))
    self.assertCheckpointState(
        model_checkpoint_path=s2,
        all_model_checkpoint_paths=[s3, s2],
        save_dir=save_dir)

    # Adding s1 (s3 should now be deleted as oldest in list)
    s1 = save2.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([s2, s1], save2.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
    self.assertFalse(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s3)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s2)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s1)))
    self.assertCheckpointState(
        model_checkpoint_path=s1,
        all_model_checkpoint_paths=[s2, s1],
        save_dir=save_dir)

    # Exercise the third helper.

    # Adding s2 again (but helper is unaware of previous s2)
    s2 = save3.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([s2], save3.last_checkpoints)
    # Created by the first helper.
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s1)))
    # Deleted by the first helper.
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
    self.assertFalse(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s3)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s2)))
    # Even though the file for s1 exists, this saver isn't aware of it, which
    # is why it doesn't end up in the checkpoint state.
    self.assertCheckpointState(
        model_checkpoint_path=s2,
        all_model_checkpoint_paths=[s2],
        save_dir=save_dir)

    # Adding s1 (s3 should not be deleted because helper is unaware of it)
    s1 = save3.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([s2, s1], save3.last_checkpoints)
    self.assertFalse(checkpoint_management.checkpoint_exists(s3))
    self.assertFalse(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s3)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s2)))
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertTrue(
        checkpoint_management.checkpoint_exists(
            checkpoint_management.meta_graph_filename(s1)))
    self.assertCheckpointState(
        model_checkpoint_path=s1,
        all_model_checkpoint_paths=[s2, s1],
        save_dir=save_dir)
