# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    mock_hook = FakeHook()
    mock_hook2 = FakeHook()
    mon_sess = monitored_session._HookedSession(
        sess=sess, hooks=[mock_hook, mock_hook2])
    a_tensor = constant_op.constant([0], name='a_tensor')
    another_tensor = constant_op.constant([5], name='another_tensor')
    third_tensor = constant_op.constant([10], name='third_tensor')
    mock_hook.request = session_run_hook.SessionRunArgs([another_tensor])
    mock_hook2.request = session_run_hook.SessionRunArgs([third_tensor])
    self.evaluate(variables.global_variables_initializer())

    output = mon_sess.run(fetches=a_tensor)
    self.assertEqual(output, [0])
    self.assertEqual(mock_hook.last_run_values.results, [5])
    self.assertEqual(mock_hook2.last_run_values.results, [10])
