# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_saving_restoring_checkpoint')
fake_hook = FakeHook()
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    with monitored_session.MonitoredTrainingSession(
        is_chief=True,
        checkpoint_dir=logdir,
        chief_only_hooks=[fake_hook],
        save_checkpoint_secs=0) as session:
        self.assertEqual(0, session.run(gstep))
        self.assertEqual(1, session.run(do_step))
        self.assertEqual(2, session.run(do_step))

    # Check whether custom hook called or not
    self.assertEqual(1, fake_hook.call_counter['begin'])
    # A restart will not find the checkpoint, since we didn't save.
    with monitored_session.MonitoredTrainingSession(
        is_chief=True, checkpoint_dir=logdir) as session:
        self.assertEqual(0, session.run(gstep))
