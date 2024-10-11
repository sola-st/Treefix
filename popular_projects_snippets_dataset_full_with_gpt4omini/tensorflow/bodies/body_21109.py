# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    with monitored_session.SingularMonitoredSession() as session:
        self.assertTrue(isinstance(session.raw_session(), session_lib.Session))
