# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    mock_time.return_value = MOCK_START_TIME
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir, save_secs=2, scaffold=self.scaffold)
    hook.begin()
    self.scaffold.finalize()

    with session_lib.Session() as sess:
        sess.run(self.scaffold.init_op)
        mon_sess = monitored_session._HookedSession(sess, [hook])

        mock_time.return_value = MOCK_START_TIME
        mon_sess.run(self.train_op)  # Saved.

        mock_time.return_value = MOCK_START_TIME + 0.5
        mon_sess.run(self.train_op)  # Not saved.

        self.assertEqual(1,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))

        # Simulate 2.5 seconds of sleep.
        mock_time.return_value = MOCK_START_TIME + 2.5
        mon_sess.run(self.train_op)  # Saved.

        mock_time.return_value = MOCK_START_TIME + 2.6
        mon_sess.run(self.train_op)  # Not saved.

        mock_time.return_value = MOCK_START_TIME + 2.7
        mon_sess.run(self.train_op)  # Not saved.

        self.assertEqual(3,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))

        # Simulate 7.5 more seconds of sleep (10 seconds from start.
        mock_time.return_value = MOCK_START_TIME + 10
        mon_sess.run(self.train_op)  # Saved.
        self.assertEqual(6,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))
