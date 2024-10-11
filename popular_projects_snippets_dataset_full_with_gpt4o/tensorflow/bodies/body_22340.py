# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    scaffold = monitored_session.Scaffold()
    training_util.get_or_create_global_step()
    train_op = training_util._increment_global_step(1)
    listener = MockCheckpointSaverListener()
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir, save_steps=1, scaffold=scaffold, listeners=[listener])
    with monitored_session.SingularMonitoredSession(
        hooks=[hook], scaffold=scaffold,
        checkpoint_dir=self.model_dir) as sess:
        sess.run(train_op)
        self.assertFalse(sess.should_stop())
        sess.run(train_op)
        self.assertFalse(sess.should_stop())
        listener.ask_for_stop = True
        sess.run(train_op)
        self.assertTrue(sess.should_stop())
