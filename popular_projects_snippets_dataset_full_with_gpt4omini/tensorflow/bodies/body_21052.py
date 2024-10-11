# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that regular exceptions reported to the coordinator from a thread
# passes through returning from a "with MonitoredSession" block and
# set the session in stop mode.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    session = monitored_session.MonitoredSession()
    with self.assertRaisesRegex(RuntimeError, 'a thread wants to stop'):
        with session:
            self.assertEqual(0, session.run(gstep))
            # Report an exception through the coordinator.
            try:
                raise RuntimeError('a thread wants to stop')
            except RuntimeError as e:
                session._coordinated_creator.coord.request_stop(e)
            self.assertTrue(session.should_stop())
