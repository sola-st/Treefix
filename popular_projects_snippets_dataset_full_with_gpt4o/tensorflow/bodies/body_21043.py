# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that we silently retry on abort during initialization.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    self.init_raised_aborted_error = False

    def _init_fn(scaffold, session):
        _, _ = scaffold, session
        if not self.init_raised_aborted_error:
            self.init_raised_aborted_error = True
            raise errors_impl.AbortedError(None, None, 'Abort')

    with monitored_session.MonitoredSession(
        session_creator=monitored_session.ChiefSessionCreator(
            scaffold=monitored_session.Scaffold(
                init_fn=_init_fn))) as session:
        self.assertFalse(session.should_stop())
        self.assertEqual(0, session.run(gstep))
    self.assertTrue(self.init_raised_aborted_error)
