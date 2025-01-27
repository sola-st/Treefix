# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    scaffold = monitored_session.Scaffold()
    self.assertEqual(None, scaffold.init_op)
    self.assertEqual(None, scaffold.init_feed_dict)
    self.assertEqual(None, scaffold.init_fn)
    self.assertEqual(None, scaffold.ready_op)
    self.assertEqual(None, scaffold.ready_for_local_init_op)
    self.assertEqual(None, scaffold.local_init_op)
    self.assertEqual(None, scaffold.saver)
