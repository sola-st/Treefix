# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
# if it runs every iteration, first iteration has None duration.
with ops.Graph().as_default(), session_lib.Session() as sess:
    t = constant_op.constant(42.0, name='foo')
    train_op = constant_op.constant(3)
    hook = basic_session_run_hooks.LoggingTensorHook(
        tensors={'foo': t}, every_n_iter=1)
    hook.begin()
    mon_sess = monitored_session._HookedSession(sess, [hook])
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess.run(train_op)
    self.assertRegex(str(self.logged_message), 'foo')
    # in first run, elapsed time is None.
    self.assertEqual(str(self.logged_message).find('sec'), -1)
