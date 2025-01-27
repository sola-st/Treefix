# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default() as g:
    a_var = variables.VariableV1(0)
    monitored_session.Scaffold().finalize()
    with monitored_session.MonitoredSession() as session:
        self.assertEqual(0, session.run(a_var))
        self.assertTrue(g.finalized)
    self.assertTrue(g.finalized)
