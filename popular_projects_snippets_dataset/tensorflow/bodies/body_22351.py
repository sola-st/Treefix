# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir, save_steps=1, scaffold=self.scaffold,
        save_graph_def=False)
    hook.begin()
    self.scaffold.finalize()
    with session_lib.Session() as sess:
        sess.run(self.scaffold.init_op)
        mon_sess = monitored_session._HookedSession(sess, [hook])
        sess.run(self.scaffold.init_op)
        hook.after_create_session(sess, None)

        self.assertNotIn('graph.pbtxt', os.listdir(self.model_dir))
        # Should have a single .meta file for step 0
        self.assertEmpty(gfile.Glob(os.path.join(self.model_dir, '*.meta')))

        mon_sess.run(self.train_op)
        self.assertEmpty(gfile.Glob(os.path.join(self.model_dir, '*.meta')))
