# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
fake_summary_writer.FakeSummaryWriter.install()
writer_cache.FileWriterCache.clear()
summary_writer = writer_cache.FileWriterCache.get(self.model_dir)

with self.graph.as_default():
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir, save_steps=2, scaffold=self.scaffold)
    hook.begin()
    self.scaffold.finalize()
    with session_lib.Session() as sess:
        sess.run(self.scaffold.init_op)
        mon_sess = monitored_session._HookedSession(sess, [hook])
        hook.after_create_session(sess, None)
        mon_sess.run(self.train_op)
    summary_writer.assert_summaries(
        test_case=self,
        expected_logdir=self.model_dir,
        expected_added_meta_graphs=[
            meta_graph.create_meta_graph_def(
                graph_def=self.graph.as_graph_def(add_shapes=True),
                saver_def=self.scaffold.saver.saver_def)
        ])

fake_summary_writer.FakeSummaryWriter.uninstall()
