# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that regular exceptions in "with body" are seen outside.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    session = monitored_session.MonitoredSession()
    # We should see that exception.
    with self.assertRaisesRegex(RuntimeError, 'regular exception'):
        with session:
            self.assertEqual(1, session.run(do_step))
            self.assertEqual(2, session.run(do_step))
            self.assertFalse(session.should_stop())
            # Will be visible outside the "with body".
            raise RuntimeError('regular exception')
      # Should have closed.
    self.assertTrue(session.should_stop())
    self.assertTrue(session._is_closed())
