# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that regular exceptions just pass through a "with
# MonitoredSession" block and set the session in stop mode.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    hook = RaiseOnceAtCountN(4, RuntimeError('regular exception'))
    session = monitored_session.MonitoredSession(hooks=[hook])
    with self.assertRaisesRegex(RuntimeError, 'regular exception'):
        with session:
            self.assertEqual(0, session.run(gstep))
            self.assertEqual(1, session.run(do_step))
            self.assertEqual(2, session.run(do_step))
            self.assertFalse(session.should_stop())
            # This triggers the hook and raises the exception
            session.run(do_step)
            # We should not hit this
            self.assertFalse(True)
    self.assertTrue(hook.raised)
    self.assertTrue(session.should_stop())
