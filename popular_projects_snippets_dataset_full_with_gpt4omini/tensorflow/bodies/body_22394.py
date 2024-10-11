# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
# Pick a fixed start time.
with self.graph.as_default():
    mock_time.return_value = MOCK_START_TIME
    hook = basic_session_run_hooks.ProfilerHook(
        save_secs=2, output_dir=self.output_dir)
    with monitored_session.SingularMonitoredSession(hooks=[hook]) as sess:
        sess.run(self.train_op)  # Not saved.
        self.assertEqual(0, self._count_timeline_files())
        # Simulate 2.5 seconds of sleep.
        mock_time.return_value = MOCK_START_TIME + 2.5
        sess.run(self.train_op)  # Saved.
        self.assertEqual(1, self._count_timeline_files())

        # Pretend some small amount of time has passed.
        mock_time.return_value = MOCK_START_TIME + 2.6
        sess.run(self.train_op)  # Not saved.
        # Edge test just before we should save the timeline.
        mock_time.return_value = MOCK_START_TIME + 4.4
        sess.run(self.train_op)  # Not saved.
        self.assertEqual(1, self._count_timeline_files())

        mock_time.return_value = MOCK_START_TIME + 4.5
        sess.run(self.train_op)  # Saved.
        self.assertEqual(2, self._count_timeline_files())
