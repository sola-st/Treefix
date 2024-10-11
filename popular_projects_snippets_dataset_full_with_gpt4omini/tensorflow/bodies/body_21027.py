# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    mock_hook = FakeHook()
    mock_hook2 = FakeHook()
    mon_sess = monitored_session._HookedSession(
        sess=sess, hooks=[mock_hook, mock_hook2])
    a_tensor = constant_op.constant([0], name='a_tensor')
    b_tensor = constant_op.constant([0], name='b_tensor')
    add_tensor = a_tensor + b_tensor
    mock_hook.request = session_run_hook.SessionRunArgs(
        None, feed_dict={a_tensor: [5]})
    mock_hook2.request = session_run_hook.SessionRunArgs(
        None, feed_dict={b_tensor: [10]})
    self.evaluate(variables.global_variables_initializer())

    self.assertEqual(mon_sess.run(fetches=add_tensor), [15])
