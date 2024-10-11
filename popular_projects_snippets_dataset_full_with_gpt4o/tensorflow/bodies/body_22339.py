# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    scaffold = monitored_session.Scaffold()
    global_step = training_util.get_or_create_global_step()
    train_op = training_util._increment_global_step(1)
    listener = MockCheckpointSaverListener()
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir,
        save_steps=1,
        scaffold=scaffold,
        listeners=[listener])
    with monitored_session.SingularMonitoredSession(
        hooks=[hook],
        scaffold=scaffold,
        checkpoint_dir=self.model_dir) as sess:
        sess.run(train_op)
        sess.run(train_op)
        global_step_val = sess.raw_session().run(global_step)
    listener_counts = listener.get_counts()
self.assertEqual(2, global_step_val)
self.assertEqual({
    'begin': 1,
    'before_save': 3,
    'after_save': 3,
    'end': 1
}, listener_counts)
