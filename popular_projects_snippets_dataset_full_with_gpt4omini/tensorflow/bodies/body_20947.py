# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_save_checkpoint_secs')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    new_gstep = state_ops.assign_add(gstep, 1)
    with monitored_session.MonitoredTrainingSession(
        is_chief=True,
        checkpoint_dir=logdir,
        save_checkpoint_secs=0.1,
        log_step_count_steps=10) as session:
        session.run(new_gstep)
        time.sleep(0.2)
        for _ in range(10):
            session.run(new_gstep)
      # A restart will find the checkpoint and recover automatically.
    with monitored_session.MonitoredTrainingSession(
        is_chief=True, checkpoint_dir=logdir) as session:
        self.assertEqual(11, session.run(gstep))
