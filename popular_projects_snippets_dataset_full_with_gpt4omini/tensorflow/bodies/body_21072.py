# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():

    def step_fn(step_context, extra_foo):
        del step_context, extra_foo

    with monitored_session.MonitoredSession() as session:
        with self.assertRaisesRegex(
            ValueError,
            '`step_fn` may either have one `step_context` argument'):
            self.assertEqual(None, session.run_step_fn(step_fn))
