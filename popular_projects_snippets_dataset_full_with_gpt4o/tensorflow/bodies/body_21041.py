# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_recovery')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    scaffold = monitored_session.Scaffold()
    # Use a hook to save the model every 100 steps.  It also saves it at
    # the end.
    hooks = [
        basic_session_run_hooks.CheckpointSaverHook(
            logdir, save_steps=1, scaffold=scaffold)
    ]
    with monitored_session.MonitoredSession(
        session_creator=monitored_session.ChiefSessionCreator(
            scaffold, checkpoint_dir=logdir),
        hooks=hooks) as session:
        self.assertEqual(0, session.run(gstep))
        self.assertEqual(1, session.run(do_step))
        self.assertEqual(2, session.run(do_step))
    # A restart will find the checkpoint and recover automatically.
    with monitored_session.MonitoredSession(
        session_creator=monitored_session.ChiefSessionCreator(
            scaffold, checkpoint_dir=logdir)) as session:
        self.assertEqual(2, session.run(gstep))
    # A restart will find the checkpoint and recover automatically.
    with monitored_session.MonitoredSession(
        session_creator=monitored_session.ChiefSessionCreator(
            scaffold,
            checkpoint_filename_with_path=checkpoint_management.
            latest_checkpoint(logdir))) as session:
        self.assertEqual(2, session.run(gstep))
