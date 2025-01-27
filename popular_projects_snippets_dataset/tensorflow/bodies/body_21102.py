# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    a_var = variables.VariableV1(0)
    with monitored_session.SingularMonitoredSession() as session:
        # If it's not initialized, following statement raises an error.
        self.assertEqual(0, session.run(a_var))
