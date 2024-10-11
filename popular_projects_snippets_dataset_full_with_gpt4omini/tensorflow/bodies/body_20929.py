# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    scaffold = monitored_session.Scaffold()
    variables.VariableV1(1, name='my_var')
    variables.VariableV1(
        2, name='my_local_var', collections=[ops.GraphKeys.LOCAL_VARIABLES])
    scaffold.finalize()
    self.assertTrue(isinstance(scaffold.init_op, ops.Operation))
    self.assertEqual(None, scaffold.init_feed_dict)
    self.assertEqual(None, scaffold.init_fn)
    self.assertTrue(isinstance(scaffold.ready_op, ops.Tensor))
    self.assertTrue(isinstance(scaffold.ready_for_local_init_op, ops.Tensor))
    self.assertTrue(isinstance(scaffold.local_init_op, ops.Operation))
    self.assertEqual(None, scaffold.local_init_feed_dict)
    self.assertTrue(isinstance(scaffold.saver, saver_lib.Saver))
    with self.cached_session() as sess:
        self.assertItemsEqual([b'my_var', b'my_local_var'],
                              sess.run(scaffold.ready_op))
        self.assertItemsEqual([b'my_var'],
                              sess.run(scaffold.ready_for_local_init_op))
        sess.run(scaffold.init_op)
        self.assertEqual(0, len(sess.run(scaffold.ready_for_local_init_op)))
        sess.run(scaffold.local_init_op)
        self.assertEqual(0, len(sess.run(scaffold.ready_op)))
