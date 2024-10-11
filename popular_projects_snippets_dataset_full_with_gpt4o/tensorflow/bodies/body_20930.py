# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    scaffold = monitored_session.Scaffold()
    constant_op.constant(1, name='my_const')
    scaffold.finalize()
    self.assertTrue(isinstance(scaffold.init_op, ops.Operation))
    self.assertEqual(None, scaffold.init_feed_dict)
    self.assertEqual(None, scaffold.init_fn)
    self.assertTrue(isinstance(scaffold.ready_op, ops.Tensor))
    self.assertTrue(isinstance(scaffold.ready_for_local_init_op, ops.Tensor))
    self.assertTrue(isinstance(scaffold.local_init_op, ops.Operation))
    self.assertEqual(None, scaffold.local_init_feed_dict)
    self.assertTrue(isinstance(scaffold.saver, saver_lib.Saver))
