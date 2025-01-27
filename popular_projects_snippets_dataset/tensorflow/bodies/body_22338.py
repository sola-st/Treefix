# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    listener = MockCheckpointSaverListener()
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir,
        save_secs=2,
        scaffold=self.scaffold,
        listeners=[listener])
    hook.begin()
    self.scaffold.finalize()
    with session_lib.Session() as sess:
        sess.run(self.scaffold.init_op)
        mon_sess = monitored_session._HookedSession(sess, [hook])
        mon_sess.run(self.train_op)  # hook runs here
        mon_sess.run(self.train_op)  # hook won't run here, so it does at end
        hook.end(sess)  # hook runs here
    self.assertEqual({
        'begin': 1,
        'before_save': 2,
        'after_save': 2,
        'end': 1
    }, listener.get_counts())
