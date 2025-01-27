# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    mock_hook = FakeHook()
    mock_hook2 = FakeHook()
    mon_sess = monitored_session._HookedSession(
        sess=sess, hooks=[mock_hook, mock_hook2])
    constant_op.constant([0], name='a_tensor')
    self.evaluate(variables.global_variables_initializer())

    mon_sess.run(fetches='a_tensor')
    self.assertFalse(mon_sess.should_stop())

    mock_hook.should_stop = True
    mon_sess.run(fetches='a_tensor')
    self.assertTrue(mon_sess.should_stop())
