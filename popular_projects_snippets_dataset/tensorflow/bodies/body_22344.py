# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    mock_time.return_value = MOCK_START_TIME
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

        mock_time.return_value = MOCK_START_TIME + 0.5
        mon_sess.run(self.train_op)  # hook runs here

        mock_time.return_value = MOCK_START_TIME + 0.5
        mon_sess.run(self.train_op)

        mock_time.return_value = MOCK_START_TIME + 3.0
        mon_sess.run(self.train_op)  # hook runs here

        mock_time.return_value = MOCK_START_TIME + 3.5
        mon_sess.run(self.train_op)

        mock_time.return_value = MOCK_START_TIME + 4.0
        mon_sess.run(self.train_op)

        mock_time.return_value = MOCK_START_TIME + 6.5
        mon_sess.run(self.train_op)  # hook runs here

        mock_time.return_value = MOCK_START_TIME + 7.0
        mon_sess.run(self.train_op)  # hook won't run here, so it does at end

        mock_time.return_value = MOCK_START_TIME + 7.5
        hook.end(sess)  # hook runs here
    self.assertEqual({
        'begin': 1,
        'before_save': 4,
        'after_save': 4,
        'end': 1
    }, listener.get_counts())
