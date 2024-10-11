# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as test_session:
    session_creator = CountingSessionCreator(test_session)
    hook = StopCoordinatorWithException(
        calls_before_stopping=2,
        exception_to_raise=errors_impl.UnknownError(
            None, None, 'Some fatal exception inside the coordinator.'))
    session = monitored_session.MonitoredSession(session_creator, [hook])

    self.assertEqual(1, session_creator.number_of_sessions_created)
    self.assertFalse(session.should_stop())

    c = constant_op.constant(0)
    v = array_ops.identity(c)

    def feed_step_fn(value):
        def step_fn(step_context):
            exit(step_context.run_with_hooks(fetches=v, feed_dict={c: value}))
        exit(step_fn)

    # The coordinator will not abort during this call, since it's the call
    # number 0.
    self.assertEqual(51, session.run_step_fn(feed_step_fn(51)))
    self.assertFalse(session.should_stop())
    # The coordinator will abort during the next call, since it's the call
    # number 1.
    self.assertEqual(42, session.run_step_fn(feed_step_fn(42)))
    # The coordinator was asked to stop due to non-redeemable error. Training
    # should stop and the session should not be recreated.
    self.assertTrue(session.should_stop())
    self.assertEqual(1, session_creator.number_of_sessions_created)
    with self.assertRaises(errors_impl.UnknownError):
        session.close()
