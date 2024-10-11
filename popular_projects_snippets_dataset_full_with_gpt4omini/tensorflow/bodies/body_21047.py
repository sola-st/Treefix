# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that we silently retry and recover on abort.  This test uses
# a CheckpointSaver to have something to recover from.
logdir = _test_dir(self.get_temp_dir(),
                   'test_recover_and_retry_on_aborted_error')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    scaffold = monitored_session.Scaffold()
    abort_hook = RaiseOnceAtCountN(
        4, errors_impl.AbortedError(None, None, 'Abort'))
    # Save after each step.
    ckpt_hook = basic_session_run_hooks.CheckpointSaverHook(
        logdir, save_steps=1, scaffold=scaffold)
    hooks = [abort_hook, ckpt_hook]
    with monitored_session.MonitoredSession(
        session_creator=monitored_session.ChiefSessionCreator(
            scaffold, checkpoint_dir=logdir),
        hooks=hooks) as session:
        self.assertEqual(0, session.run(gstep))
        self.assertEqual(1, session.run(do_step))
        self.assertEqual(2, session.run(do_step))
        self.assertFalse(session.should_stop())
        # Here at step 3, the hook triggers and raises AbortedError.  The
        # MonitoredSession automatically restores and retries.
        self.assertEqual(3, session.run(do_step))
        self.assertTrue(abort_hook.raised)
        self.assertFalse(session.should_stop())
        self.assertEqual(4, session.run(do_step))
        self.assertFalse(session.should_stop())
