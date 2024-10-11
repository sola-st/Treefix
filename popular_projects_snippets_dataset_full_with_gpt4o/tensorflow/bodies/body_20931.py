# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    variables.VariableV1([1])
    scaffold1 = monitored_session.Scaffold()
    scaffold1.finalize()
    scaffold2 = monitored_session.Scaffold()
    scaffold2.finalize()
    self.assertEqual(scaffold1.init_op, scaffold2.init_op)
    self.assertEqual(scaffold1.ready_op, scaffold2.ready_op)
    self.assertEqual(scaffold1.ready_for_local_init_op,
                     scaffold2.ready_for_local_init_op)
    self.assertEqual(scaffold1.local_init_op, scaffold2.local_init_op)
    self.assertEqual(scaffold1.saver, scaffold2.saver)
