# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_saving_restoring_checkpoint')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    with monitored_session.MonitoredTrainingSession(
        is_chief=True, checkpoint_dir=logdir) as session:
        self.assertEqual(0, session.run(gstep))
        self.assertEqual(1, session.run(do_step))
        self.assertEqual(2, session.run(do_step))
    # A restart will find the checkpoint and recover automatically.
    with monitored_session.MonitoredTrainingSession(
        is_chief=True, checkpoint_dir=logdir) as session:
        self.assertEqual(2, session.run(gstep))
