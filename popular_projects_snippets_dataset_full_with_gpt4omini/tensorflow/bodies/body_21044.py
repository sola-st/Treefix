# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that we silently retry on error.  Note that this does not test
# recovery as we do not use a CheckpointSaver in this test.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    hook = RaiseOnceAtCountN(4, ex)
    with monitored_session.MonitoredSession(hooks=[hook]) as session:
        self.assertEqual(0, session.run(gstep))
        self.assertEqual(1, session.run(do_step))
        self.assertEqual(2, session.run(do_step))
        self.assertFalse(session.should_stop())
        # Here at step 3, the hook triggers and raises AbortedError.  The
        # MonitoredSession automatically retries and restart from a freshly
        # initialized session, so the step is back to 0 and running do_step
        # moves it to 1.
        self.assertEqual(1, session.run(do_step))
        self.assertFalse(session.should_stop())
        self.assertTrue(hook.raised)
        self.assertEqual(2, session.run(do_step))
        self.assertFalse(session.should_stop())
