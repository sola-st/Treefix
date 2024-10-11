# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    variables.VariableV1([1])
    saver = saver_lib.Saver()
    scaffold = monitored_session.Scaffold(
        init_op=2,
        init_feed_dict=3,
        init_fn=lambda scaffold, sess: 4,
        ready_op=5,
        ready_for_local_init_op=6,
        local_init_op=7,
        local_init_feed_dict=8,
        saver=saver)
    scaffold.finalize()
    self.assertEqual(2, scaffold.init_op)
    self.assertEqual(3, scaffold.init_feed_dict)
    self.assertTrue(callable(scaffold.init_fn))
    self.assertEqual(5, scaffold.ready_op)
    self.assertEqual(6, scaffold.ready_for_local_init_op)
    self.assertEqual(7, scaffold.local_init_op)
    self.assertEqual(8, scaffold.local_init_feed_dict)
    self.assertEqual(saver, scaffold.saver)
