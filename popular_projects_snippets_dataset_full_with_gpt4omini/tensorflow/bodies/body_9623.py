# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    b = control_flow_ops.no_op()  # An op, not a tensor.
    c = constant_op.constant(44.0)
    res = sess.run({'a': a, 'b': b, 'c': c})
    self.assertIsInstance(res, dict)
    self.assertEqual(42.0, res['a'])
    self.assertIsNone(res['b'])
    self.assertEqual(44.0, res['c'])
