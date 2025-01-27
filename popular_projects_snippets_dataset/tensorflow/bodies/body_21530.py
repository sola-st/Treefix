# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_dir = self._get_test_dir("keep_checkpoint_every_n_hours")

with self.cached_session() as sess:
    v = variable_scope.variable([10.0], name="v")
    # Run the initializer NOW to avoid the 0.5s overhead of the first Run()
    # call, which throws the test timing off in fastbuild mode.
    self.evaluate(variables.global_variables_initializer())
    # Create a saver that will keep the last 2 checkpoints plus one every 0.7
    # seconds.
    start_time = time.time()
    mock_time.time.return_value = start_time
    save = saver_module.Saver(
        {
            "v": v
        }, max_to_keep=2, keep_checkpoint_every_n_hours=0.7 / 3600)
    self.assertEqual([], save.last_checkpoints)

    # Wait till 1 seconds have elapsed so s1 will be old enough to keep.
    # sleep may return early, don't trust it.
    mock_time.time.return_value = start_time + 1.0
    s1 = save.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([s1], save.last_checkpoints)

    s2 = save.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([s1, s2], save.last_checkpoints)

    # We now have 2 'last_checkpoints': [s1, s2].  The next call to Save(),
    # would normally delete s1, because max_to_keep is 2.  However, s1 is
    # older than 0.7s so we must keep it.
    s3 = save.save(sess, os.path.join(save_dir, "s3"))
    self.assertEqual([s2, s3], save.last_checkpoints)

    # s1 should still be here, we are Not checking now to reduce time
    # variance in the test.

    # We now have 2 'last_checkpoints': [s2, s3], and s1 on disk.  The next
    # call to Save(), will delete s2, because max_to_keep is 2, and because
    # we already kept the old s1. s2 is very close in time to s1 so it gets
    # deleted.
    s4 = save.save(sess, os.path.join(save_dir, "s4"))
    self.assertEqual([s3, s4], save.last_checkpoints)

    # Check that s1 is still here, but s2 is gone.
    self.assertTrue(checkpoint_management.checkpoint_exists(s1))
    self.assertFalse(checkpoint_management.checkpoint_exists(s2))
    self.assertTrue(checkpoint_management.checkpoint_exists(s3))
    self.assertTrue(checkpoint_management.checkpoint_exists(s4))
