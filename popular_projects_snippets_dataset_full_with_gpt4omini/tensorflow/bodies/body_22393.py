# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    hook = basic_session_run_hooks.ProfilerHook(
        save_secs=2, output_dir=self.output_dir)
    with monitored_session.SingularMonitoredSession(hooks=[hook]) as sess:
        sess.run(self.train_op)
        self.assertEqual(0, self._count_timeline_files())
