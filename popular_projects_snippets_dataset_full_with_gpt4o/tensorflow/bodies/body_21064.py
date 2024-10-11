# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():

    def step_fn(step_context):
        step_context.request_stop()

    with monitored_session.MonitoredSession() as session:
        self.assertEqual(None, session.run_step_fn(step_fn))
        self.assertTrue(session.should_stop())
