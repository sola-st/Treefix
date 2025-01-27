# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    def step_fn(step_context):
        step_context.request_stop()

    with monitored_session.MonitoredSession() as session:
        while not session.should_stop():
            _ = session.run_step_fn(step_fn)
            self.fail('An exception should be raised on the line above.')
