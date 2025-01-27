# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as test_session:
    session_creator = CountingSessionCreator(test_session)
    session = self.create_raw_session_with_failing_coordinator(
        session_creator,
        FailTrainingAfterCoordinatorStopped(calls_before_stopping=2))

    self.assertEqual(1, session_creator.number_of_sessions_created)
    self.assertFalse(session.should_stop())

    c = constant_op.constant(0)
    v = array_ops.identity(c)

    def feed_step_fn(value):

        def step_fn(step_context):
            exit(step_context.run_with_hooks(fetches=v, feed_dict={c: value}))

        exit(step_fn)

    # Training will not fail, since it's the call number 0.
    self.assertEqual(51, session.run_step_fn(feed_step_fn(51)))
    self.assertFalse(session.should_stop())
    # Training will fail during the next call, since it's the call
    # number 1.
    self.assertEqual(42, session.run_step_fn(feed_step_fn(42)))
    # Even though the coordinator stopped which and training failed, the
    # underlying session is recreated and training is to be continued.
    self.assertFalse(session.should_stop())
    self.assertEqual(2, session_creator.number_of_sessions_created)
