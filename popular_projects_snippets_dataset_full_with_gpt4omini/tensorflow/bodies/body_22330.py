# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    t = constant_op.constant(42.0, name='foo')
    train_op = constant_op.constant(3)
    hook = basic_session_run_hooks.LoggingTensorHook(
        tensors=[t.name], every_n_iter=10,
        formatter=lambda items: 'qqq=%s' % items[t.name])
    hook.begin()
    mon_sess = monitored_session._HookedSession(sess, [hook])
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess.run(train_op)
    self.assertEqual(self.logged_message[0], 'qqq=42.0')
