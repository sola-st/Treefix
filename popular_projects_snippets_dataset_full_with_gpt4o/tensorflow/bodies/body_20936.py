# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    variables.VariableV1([1])
    saver = saver_lib.Saver()
    scaffold1 = monitored_session.Scaffold(
        init_op=2,
        init_feed_dict=3,
        init_fn=lambda scaffold, sess: 4,
        ready_op=5,
        ready_for_local_init_op=6,
        local_init_op=7,
        local_init_feed_dict=8,
        saver=saver)

    scaffold2 = monitored_session.Scaffold(
        init_op=4,
        init_feed_dict=6,
        init_fn=lambda scaffold, sess: 8,
        ready_op=10,
        ready_for_local_init_op=12,
        local_init_op=14,
        local_init_feed_dict=15,
        saver=saver,
        copy_from_scaffold=scaffold1)

    scaffold2.finalize()
    self.assertEqual(4, scaffold2.init_op)
    self.assertEqual(6, scaffold2.init_feed_dict)
    self.assertTrue(callable(scaffold2.init_fn))
    self.assertEqual(10, scaffold2.ready_op)
    self.assertEqual(12, scaffold2.ready_for_local_init_op)
    self.assertEqual(14, scaffold2.local_init_op)
    self.assertEqual(15, scaffold2.local_init_feed_dict)
    self.assertEqual(saver, scaffold2.saver)
