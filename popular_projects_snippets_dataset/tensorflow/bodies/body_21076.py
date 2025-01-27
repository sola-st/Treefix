# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():

    class Model:

        def step_fn(self, step_context, extra_foo):
            del step_context, extra_foo

    with monitored_session.MonitoredSession() as session:
        with self.assertRaisesRegex(
            ValueError,
            '`step_fn` may either have one `step_context` argument'):
            model = Model()
            self.assertEqual(None, session.run_step_fn(model.step_fn))
