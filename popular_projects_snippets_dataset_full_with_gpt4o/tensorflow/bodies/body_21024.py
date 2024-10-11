# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    mock_hook = FakeHook()
    mock_hook2 = FakeHook()
    mon_sess = monitored_session._HookedSession(
        sess=sess, hooks=[mock_hook, mock_hook2])
    a_tensor = constant_op.constant([0], name='a_tensor')
    self.evaluate(variables.global_variables_initializer())
    mon_sess.run(a_tensor)

    for hook in [mock_hook, mock_hook2]:
        self.assertEqual(
            hook.last_run_values,
            session_run_hook.SessionRunValues(
                results=None,
                options=config_pb2.RunOptions(),
                run_metadata=config_pb2.RunMetadata()))
        self.assertEqual(hook.last_run_context.original_args,
                         session_run_hook.SessionRunArgs(a_tensor))
        self.assertEqual(hook.last_run_context.session, sess)
        self.assertEqual(hook.call_counter['begin'], 0)
        self.assertEqual(hook.call_counter['after_create_session'], 0)
        self.assertEqual(hook.call_counter['before_run'], 1)
        self.assertEqual(hook.call_counter['after_run'], 1)
