# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
scaffold1 = monitored_session.Scaffold()
with ops.Graph().as_default():
    variables.VariableV1([1])
    saver = saver_lib.Saver()
    scaffold2 = monitored_session.Scaffold(
        init_op=2,
        init_feed_dict=3,
        init_fn=lambda scaffold, sess: 4,
        ready_op=5,
        ready_for_local_init_op=6,
        local_init_op=7,
        local_init_feed_dict=8,
        saver=saver,
        copy_from_scaffold=scaffold1)

    scaffold2.finalize()
    self.assertEqual(2, scaffold2.init_op)
    self.assertEqual(3, scaffold2.init_feed_dict)
    self.assertTrue(callable(scaffold2.init_fn))
    self.assertEqual(5, scaffold2.ready_op)
    self.assertEqual(6, scaffold2.ready_for_local_init_op)
    self.assertEqual(7, scaffold2.local_init_op)
    self.assertEqual(8, scaffold2.local_init_feed_dict)
    self.assertEqual(saver, scaffold2.saver)
