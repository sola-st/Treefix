# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
writer_cache.FileWriterCache.clear()
fake_summary_writer.FakeSummaryWriter.install()
fake_writer = writer_cache.FileWriterCache.get(self.output_dir)
with self.graph.as_default():
    hook = basic_session_run_hooks.ProfilerHook(
        save_steps=1, output_dir=self.output_dir)
    with monitored_session.SingularMonitoredSession(hooks=[hook]) as sess:
        sess.run(self.train_op)  # Not saved.
        sess.run(self.train_op)  # Saved.
        self.assertEqual(
            list(fake_writer._added_run_metadata.keys()), ['step_2'])
fake_summary_writer.FakeSummaryWriter.uninstall()
