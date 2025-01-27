# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_save_checkpoint_steps')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    new_gstep = state_ops.assign_add(gstep, 1)
    with monitored_session.MonitoredTrainingSession(
        is_chief=True,
        checkpoint_dir=logdir,
        save_checkpoint_steps=100,
        log_step_count_steps=10) as session:
        for _ in range(100):
            session.run(new_gstep)
      # A restart will find the checkpoint and recover automatically.
    with monitored_session.MonitoredTrainingSession(
        is_chief=True, checkpoint_dir=logdir) as session:
        self.assertEqual(100, session.run(gstep))
