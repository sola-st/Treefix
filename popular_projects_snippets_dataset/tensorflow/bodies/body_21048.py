# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Tests that we stop cleanly when OutOfRange is raised.
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    hook = RaiseOnceAtCountN(2, errors_impl.OutOfRangeError(None, None,
                                                            'EOI'))
    session = monitored_session.MonitoredSession(hooks=[hook])
    # session should cleanly exit from the context.
    with session:
        self.assertEqual(0, session.run(gstep))
        self.assertFalse(session.should_stop())
        # Here at step 1, the hook triggers and raises OutOfRange. The
        # session should go into should_stop() mode. It should raise the
        # exception. So next step should not be executed.
        session.run(do_step)
        self.assertTrue(False)
    self.assertTrue(session.should_stop())
