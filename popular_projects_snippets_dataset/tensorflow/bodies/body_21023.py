# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    mock_run = FakeSession(sess)
    mon_sess = monitored_session._HookedSession(sess=mock_run, hooks=[])
    a_tensor = constant_op.constant([0], name='a_tensor')
    self.evaluate(variables.global_variables_initializer())
    output = mon_sess.run(fetches=a_tensor,
                          feed_dict='a_feed',
                          options='an_option',
                          run_metadata='a_metadata')
    self.assertEqual(output, [0])
    self.assertEqual(mock_run.args_called, {
        'feed_dict': 'a_feed',
        'options': 'an_option',
        'run_metadata': 'a_metadata'
    })
