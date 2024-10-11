# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that regular exceptions reported to the coordinator from a thread
# passes through a "run()" call within a "with MonitoredSession" block and
# set the session in stop mode.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    session = monitored_session.SingularMonitoredSession()
    run_performed_without_error = False
    with self.assertRaisesRegex(RuntimeError, 'a thread wants to stop'):
        with session:
            self.assertEqual(0, session.run(gstep))
            # Report an exception through the coordinator.
            try:
                raise RuntimeError('a thread wants to stop')
            except RuntimeError as e:
                session._coordinated_creator.coord.request_stop(e)
            # Call run() which should perform normally.
            self.assertEqual(0, session.run(gstep))
            run_performed_without_error = True
    self.assertTrue(run_performed_without_error)
