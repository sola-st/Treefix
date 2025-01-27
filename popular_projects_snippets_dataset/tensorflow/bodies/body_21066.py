# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    was_stop_iteration_raised = False

    def step_fn(step_context):
        step_context.request_stop()

    session = monitored_session.MonitoredSession()
    try:
        self.assertEqual(None, session.run_step_fn(step_fn))
    except StopIteration:
        was_stop_iteration_raised = True

    self.assertTrue(was_stop_iteration_raised)
    self.assertFalse(session.should_stop())
