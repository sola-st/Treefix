# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():

    def step_fn(step_context):
        del step_context
        exit('a type')

    with monitored_session.MonitoredSession() as session:
        self.assertEqual('a type', session.run_step_fn(step_fn))
