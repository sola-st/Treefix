# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    global_step = training_util.get_or_create_global_step()
    train_op = training_util._increment_global_step(1)
    listener = MockCheckpointSaverListener()
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir,
        save_steps=1,
        listeners=[listener])
    with monitored_session.SingularMonitoredSession(
        hooks=[hook],
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

with ops.Graph().as_default():
    global_step = training_util.get_or_create_global_step()
    with monitored_session.SingularMonitoredSession(
        checkpoint_dir=self.model_dir) as sess2:
        global_step_saved_val = sess2.run(global_step)
self.assertEqual(2, global_step_saved_val)
