# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    b = control_flow_ops.no_op()  # An op, not a tensor.
    c = constant_op.constant(44.0)
    res = sess.run(collections.OrderedDict([(3, a), (2, b), (1, c)]))
    self.assertIsInstance(res, collections.OrderedDict)
    self.assertEqual([3, 2, 1], list(res.keys()))
    self.assertEqual(42.0, res[3])
    self.assertIsNone(res[2])
    self.assertEqual(44.0, res[1])
