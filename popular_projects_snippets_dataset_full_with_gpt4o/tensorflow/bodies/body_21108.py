# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default() as g:
    with monitored_session.SingularMonitoredSession() as session:
        self.assertEqual(g, session.graph)
