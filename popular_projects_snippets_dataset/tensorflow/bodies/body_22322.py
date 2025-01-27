# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    t = constant_op.constant(42.0, name='foo')
    train_op = constant_op.constant(3)
    hook = basic_session_run_hooks.LoggingTensorHook(
        tensors=[t.name], at_end=True)
    hook.begin()
    mon_sess = monitored_session._HookedSession(sess, [hook])
    self.evaluate(variables_lib.global_variables_initializer())
    self.logged_message = ''
    for _ in range(3):
        mon_sess.run(train_op)
        # assertNotRegexpMatches is not supported by python 3.1 and later
        self.assertEqual(str(self.logged_message).find(t.name), -1)

    hook.end(sess)
    self.assertRegex(str(self.logged_message), t.name)
